import inspect
import json
from condu.conductor import TaskClient, WorkflowClient
from cdm.cli.commands import BaseApp
from cdm.cli.common.client_factory import get_task_client, get_workflow_client
from oslo_config import cfg

CONF = cfg.CONF


class ConductorActions(BaseApp):
    """Task and Workflow actions"""

    name = "ca"
    task_cmd = ['getTask', 'getTaskQueueSizes', 'getTasksInQueue', 'get_task_logs', 'removeTaskFromQueue']
    workflow_cmd = ['getRunningWorkflows', 'getWorkflow', 'pauseWorkflow', 'rerunWorkflow', 'restartWorkflow',
                    'resumeWorkflow', 'skipTaskFromWorkflow', 'startWorkflow', 'terminateWorkflow']
    commands = task_cmd + workflow_cmd

    @classmethod
    def add_handler(cls, method_name, obj, subparsers):
        parser = subparsers.add_parser(method_name, help=method_name)
        parser.set_defaults(cmd_class=cls)
        m = getattr(obj, method_name)
        args = inspect.getfullargspec(m)
        args.args.remove('self')
        for arg in args.args:
            parser.add_argument('--{}'.format(arg),
                                help=arg)

    @classmethod
    def add_argument_parser(cls, subparsers):
        task_client = TaskClient("")
        workflow_client = WorkflowClient("")
        for c in cls.task_cmd:
            cls.add_handler(c, task_client, subparsers)
        for c in cls.workflow_cmd:
            cls.add_handler(c, workflow_client, subparsers)

    @staticmethod
    def t1():
        task_client = get_workflow_client()
        print(task_client.getWorkflow('0d8e55fc-758b-43a3-90ec-452686907603', False))

    @classmethod
    def main(cls):
        task_client = get_task_client()
        workflow_client = get_workflow_client()
        to_run = CONF.command.name
        if to_run in cls.task_cmd:
            m = getattr(task_client, to_run)
        else:
            m = getattr(workflow_client, to_run)
        args = inspect.getfullargspec(m)
        args.args.remove('self')
        kwargs = {}
        for arg in args.args:
            kwargs[arg] = getattr(CONF.command, arg)
        kw = {k: v for k, v in kwargs.items() if v is not None}
        res = m(**kw)
        if res:
            try:
                print(json.dumps(res, indent=4))
            except:
                print(res)
