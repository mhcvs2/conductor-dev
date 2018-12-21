import json
from mworker.conductor import conductor
from mworker.common import config
from mworker.common.common import format_time_dict


class MetadataEx(conductor.MetadataClient):

    def _get_workflow_defs(self):
        wf_dfs = self.getAllWorkflowDefs()
        for wf_df in wf_dfs:
            format_time_dict(wf_df, 'createTime', 'updateTime')
        return wf_dfs

    def list_workflow(self, keyword=None):
        wf_dfs = self.getAllWorkflowDefs()
        if keyword:
            names = [wf_df["name"] for wf_df in wf_dfs if keyword in wf_df['name']]
        else:
            names = [wf_df["name"] for wf_df in wf_dfs]
        print json.dumps(names, indent=config.JSON_INDENT, sort_keys=True)

    def list_workflow_detail(self, keyword):
        wf_dfs = self._get_workflow_defs()
        if keyword:
            print json.dumps([wf_df for wf_df in wf_dfs if keyword in wf_df['name']],
                             indent=config.JSON_INDENT, sort_keys=True)
        else:
            print json.dumps(wf_dfs, indent=config.JSON_INDENT, sort_keys=True)

    def list_a_workflow_detail(self, name):
        wf_dfs = self._get_workflow_defs()
        for wf_df in wf_dfs:
            if wf_df['name'] == name:
                print json.dumps(wf_df, indent=config.JSON_INDENT, sort_keys=True)
                return
        print 'Workflow %s does not exist.' % name
