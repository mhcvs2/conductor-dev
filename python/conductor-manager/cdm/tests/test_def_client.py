import unittest
import json
from condu.conductor import MetadataClient


class Test(unittest.TestCase):

    def setUp(self):
        self.mdc = MetadataClient("http://tx2:8080/api")

    def test_get_all_wfd(self):
        for wfd in self.mdc.getAllWorkflowDefs():
            print("---------{}---------".format(wfd['name']))
            print(json.dumps(wfd, indent=4))

    def test_get_td(self):
        print(self.mdc.getTaskDef("task_1"))
        print(self.mdc.getTaskDef("task_100"))

    def test_get_wfd2(self):
        print(self.mdc.getWorkflowDef("sub_flow_3"))

    def test_register_wf(self):
        td = {'createTime': 1545112548640, 'name': 'sub_flow_11', 'description': 'A Simple sub-workflow with 2 tasks', 'version': 2, 'tasks': [{'name': 'task_5', 'taskReferenceName': 'task_5', 'type': 'SIMPLE', 'startDelay': 0}, {'name': 'task_6', 'taskReferenceName': 'task_6', 'type': 'SIMPLE', 'startDelay': 0}], 'schemaVersion': 2}
        # print(self.mdc.updateWorkflowDefs([td]))
        self.mdc.createWorkflowDef(td)
