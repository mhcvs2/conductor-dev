from condu.conductor import MetadataClient
from oslo_config import cfg
from cdm.tests.mock_client import MockClient

CONF = cfg.CONF


def get_metadata_client():
    return MockClient(CONF.conductor.server_url)
    # return MetadataClient(CONF.conductor.server_url)
