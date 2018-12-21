import os
import jinja2
from oslo_config import cfg
from twitter.common.dirutil import safe_mkdir
from cdm.cli.commands import BaseApp


CONF = cfg.CONF


def build_jinja_environment():
    env = jinja2.Environment(
        autoescape=True,
        loader=jinja2.ChoiceLoader([
            jinja2.PackageLoader("cdm", "templates")
        ]))
    return env


env = build_jinja_environment()


class CreateDefFile(BaseApp):
    """Create workflow/task definition file form template"""

    name = "cw"
    def_type = "workflow"

    @classmethod
    def add_argument_parser(cls, subparsers):
        parser = super(CreateDefFile, cls).add_argument_parser(subparsers)
        parser.add_argument(
            'def_name',
            help='definition name'
        )
        parser.add_argument(
            '--sub_path',
            required=False,
            help='sub path in register_check_path'
        )

    @classmethod
    def main(cls):
        root = CONF.register_check_path
        name = CONF.command.def_name
        sub_path = CONF.command.sub_path
        if sub_path:
            path = os.path.join(root, sub_path)
        else:
            path = root
        name = "{}_task".format(name) if cls.def_type == "task" else "{}_workflow".format(name)
        file_path = os.path.join(path, "{}.json".format(name))
        if os.path.isfile(file_path):
            print("file: %s is exist" % file_path)
            return
        safe_mkdir(path)
        if cls.def_type == "task":
            template = env.get_template("task.json.template")
        else:
            template = env.get_template("workflow.json.template")
        template.stream(name=name).dump(file_path)


class CreateTaskDefFile(CreateDefFile):

    name = "ct"
    def_type = "task"
