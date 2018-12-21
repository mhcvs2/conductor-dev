#!/bin/python
import sys
import time
from twitter.common import app
from mworker.conductor import conductor
from mworker.conductor.ConductorWorker import ConductorWorker
from mworker.common.common import log

# tasks: {name: {"definition":  , "handler":  }...}
tasks = {}
# workflows: {name: definition...}
workflows = {}


def register(url):
    mdc = conductor.MetadataClient(url)
    t_dfs = mdc.getAllTaskDefs()
    register_tasks = [t_df["name"] for t_df in t_dfs]
    need_register_tasks = []
    for name, task_info in tasks.items():
        if name in register_tasks:
            mdc.registerTaskDef(task_info['definition'])
        else:
            task_info['definition']['createTime'] = time.time()
            need_register_tasks.append(task_info['definition'])
    if len(need_register_tasks) > 0:
        mdc.registerTaskDefs(need_register_tasks)

    wf_dfs = mdc.getAllWorkflowDefs()
    resgister_wf = {wf_df["name"]: wf_df["version"] for wf_df in wf_dfs}
    update = []
    for workflow, definition in workflows.items():
        if workflow not in resgister_wf:
            print workflow
            definition['createTime'] = time.time()
            mdc.createWorkflowDef(definition)
        else:
            update.append(definition)
    if len(update) > 0:
        mdc.updateWorkflowDefs(update)


def execute(task):
    return apply(tasks[task["taskType"]]['handler'], (task,))


def proxy_main():
    app.add_option(
        '-s',
        '--server',
        dest='server',
        default='109.105.30.118:8080',
        help='Address for the condustor server')

    def main(args, options):
        if options.server.startswith('http://'):
            url = '{}/api'.format(options.server)
        else:
            url = 'http://{}/api'.format(options.server)
        register(url)

        cc = ConductorWorker(url, 1, 0.1)
        for task_name in tasks:
            cc.start(task_name, execute, False)
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            log.info("worker terminated.")
            sys.exit(0)

    app.main()


if __name__ == '__main__':
    proxy_main()
