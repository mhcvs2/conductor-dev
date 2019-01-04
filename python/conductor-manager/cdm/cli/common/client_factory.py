from condu.conductor import MetadataClient, TaskClient, WorkflowClient
from oslo_config import cfg
# from cdm.tests.mock_client import MockClient

CONF = cfg.CONF


def get_metadata_client():
    # return MockClient(CONF.conductor.server_url)
    return MetadataClient(CONF.conductor.server_url)


def get_task_client():
    return TaskClient(CONF.conductor.server_url)


def get_workflow_client():
    print(CONF.conductor.server_url)
    return WorkflowClient(CONF.conductor.server_url)
