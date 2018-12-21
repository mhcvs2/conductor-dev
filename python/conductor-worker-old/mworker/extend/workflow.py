import json
from mworker.conductor import conductor
from mworker.common.common import log
from mworker.common import config


class WorkflowEx(conductor.WorkflowClient):

    def stop_by_name(self, name, version):
        workflow_ids = self.getRunningWorkflows(name, version)
        for wf in workflow_ids:
            log.info('Stop workflow: %s' % wf)
            self.terminateWorkflow(wf)

    def list_running(self, name, version):
        workflow_ids = self.getRunningWorkflows(name, version)
        print json.dumps(workflow_ids, indent=config.JSON_INDENT, sort_keys=True)

    def start(self, name, version, input_data):
        try:
            input_data = json.loads(input_data)
        except:
            log.error("input %s should be a json" % input_data)
            return
        workflow_id = self.startWorkflow(name, input_data, version, None)
        log.info('workflow id: %s' % workflow_id)

    def get_workflow(self, w_id, include_task=False):
        print(json.dumps(self.getWorkflow(w_id, include_task),
                         indent=config.JSON_INDENT,
                         sort_keys=True))
