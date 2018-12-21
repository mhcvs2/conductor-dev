import os
from oslo_config import cfg
from cdm.cli.commands import BaseApp
from cdm.cli.common.client_factory import get_metadata_client
from cdm.cli.common.register_def import FlowDef
from cdm.cli.common.utils import *


CONF = cfg.CONF


class RegisterDef(BaseApp):
    """Register workflow/task definition to conductor server"""

    name = "register"

    @classmethod
    def add_argument_parser(cls, subparsers):
        parser = super(RegisterDef, cls).add_argument_parser(subparsers)
        parser.add_argument(
            '--path',
            required=False,
            help='a dir or file in json type'
        )

    @staticmethod
    def register_file(file_path, flow):
        with open(file_path, 'r') as f:
            flow.file_path = file_path
            flow.data = f.read()
            flow.register()

    @classmethod
    def main(cls):
        client = get_metadata_client()
        if not CONF.command.path:
            path = CONF.register_check_path
        elif start_with(CONF.command.path, "/"):
            path = CONF.command.path
        else:
            path = os.path.join(CONF.register_check_path, CONF.command.path)
        if not path:
            print("nothing to do")
            return
        flow = FlowDef(client)
        if os.path.isfile(path):
            cls.register_file(path, flow)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for f in files:
                    if not f.endswith(".json"):
                        continue
                    cls.register_file(os.path.join(root, f), flow)
