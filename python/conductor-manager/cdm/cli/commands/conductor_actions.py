import inspect
import json
from condu.conductor import TaskClient, WorkflowClient, MetadataClient
from cdm.cli.commands import BaseApp
from cdm.cli.common.client_factory import get_task_client, get_workflow_client, get_metadata_client
from oslo_config import cfg
from importlib import import_module

CONF = cfg.CONF


class ConductorActions(BaseApp):
    """Task and Workflow actions"""

    name = "ca"
    task_cmd = ['getTask', 'getTaskQueueSizes', 'getTasksInQueue', 'get_task_logs', 'removeTaskFromQueue']
    workflow_cmd = ['getRunningWorkflows', 'getWorkflow', 'pauseWorkflow', 'rerunWorkflow', 'restartWorkflow',
                    'resumeWorkflow', 'skipTaskFromWorkflow', 'startWorkflow', 'terminateWorkflow']
    def_cmd = ['getAllWorkflowDefs', 'getAllTaskDefs', 'getWorkflowDef', 'getTaskDef']
    commands = task_cmd + workflow_cmd + def_cmd

    bool_args = ['includeTasks']
    dict_args = ['inputjson']

    passed = ['correlationId']

    action_handlers = {}
    handler_module = import_module('cdm.cli.commands.action_handlers')
    for i in dir(handler_module):
        handler = getattr(handler_module, i)
        if inspect.isclass(handler):
            action_handlers[i.lower()] = handler

    @classmethod
    def add_handler(cls, method_name, obj, subparsers):
        parser = subparsers.add_parser(method_name, help=method_name)
        parser.set_defaults(cmd_class=cls)
        m = getattr(obj, method_name)
        args = inspect.getfullargspec(m)
        args.args.remove('self')
        if method_name.lower() in cls.action_handlers:
            getattr(cls.action_handlers.get(method_name.lower()), 'args')(args.args)
        for arg in args.args:
            if arg in cls.bool_args:
                short = arg[0]
                parser.add_argument('-{}'.format(short),
                                    '--{}'.format(arg),
                                    action='store_true',
                                    help=arg)
            elif 'name' in arg.lower() or 'id' in arg.lower() and arg not in cls.passed:
                parser.add_argument('{}'.format(arg),
                                    help=arg)
            else:
                parser.add_argument('--{}'.format(arg),
                                    help=arg)

    @classmethod
    def add_argument_parser(cls, subparsers):
        task_client = TaskClient("")
        workflow_client = WorkflowClient("")
        def_client = MetadataClient("")
        for c in cls.task_cmd:
            cls.add_handler(c, task_client, subparsers)
        for c in cls.workflow_cmd:
            cls.add_handler(c, workflow_client, subparsers)
        for c in cls.def_cmd:
            cls.add_handler(c, def_client, subparsers)

    @staticmethod
    def t1():
        task_client = get_workflow_client()
        print(task_client.startWorkflow('kitchensink', {"aa": "bb"}))

    @classmethod
    def main(cls):
        task_client = get_task_client()
        workflow_client = get_workflow_client()
        def_client = get_metadata_client()
        to_run = CONF.command.name
        if to_run in cls.task_cmd:
            m = getattr(task_client, to_run)
        elif to_run in cls.workflow_cmd:
            m = getattr(workflow_client, to_run)
        else:
            m = getattr(def_client, to_run)
        args = inspect.getfullargspec(m)
        args.args.remove('self')
        kwargs = {}
        for arg in args.args:
            data = getattr(CONF.command, arg)
            if arg in cls.dict_args:
                data = json.loads(data)
            kwargs[arg] = data
        kw = {k: v for k, v in kwargs.items() if k == 'version' or v is not None}
        if to_run.lower() in cls.action_handlers:
            res = getattr(cls.action_handlers.get(to_run.lower()), 'run')(m, kw)
        else:
            res = m(**kw)
        if res:
            try:
                print(json.dumps(res, indent=4))
            except:
                print(res)
        else:
            print("empty reply.")
