import json
from cdm.cli.common.utils import *


class FlowDef(object):

    def __init__(self, client):
        self._is_task = False
        self._data = None
        self._client = client
        self._name = None
        self._version = None
        self.file_path = ""

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, text):
        try:
            self._data = json.loads(text)
        except Exception as e:
            raise JsonFormatError(e)
        self._is_task = "tasks" not in self._data
        check_field("name", self._data, self.file_path)
        self._name = self._data["name"]
        if not self._is_task:
            check_field("version", self._data, self.file_path)
            self._version = self._data["version"]

    def register(self):
        if self._is_task:
            self.register_task()
        else:
            self.register_workflow()

    def register_task(self):
        if not self._client.getTaskDef(self._name):
            print("register task: %s" % self._name)
            self._client.registerTaskDefs([self._data])
        else:
            print("task %s is exist, ignore" % self._name)

    def register_workflow(self):
        old = self._client.getWorkflowDef(self._name)
        if not old:
            print("create workflow definition(name = %s)" % self._name)
            self._client.createWorkflowDef(self._data)
        elif old['version'] != self._version:
            print("update workflow definition from %s to %s" % (old["version"], self._version))
            self._client.updateWorkflowDefs([self._data])
