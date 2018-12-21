import os
from oslo_config import cfg
from cdm.cli.commands import register_def, create_def

CONF = cfg.CONF

CMDS = [
    register_def.RegisterDef,
    create_def.CreateDefFile,
    create_def.CreateTaskDefFile
]

common_opts = [
    cfg.StrOpt('register_check_path', default=None,
               help='A dir to find definition files'),
]

conductor_opts = [
    cfg.StrOpt('server_url',
               default="http://tx2:8080/api",
               help='Conductor server url..'
               ),
]


def add_command_parsers(subparsers):
    for cmd in CMDS:
        cmd.add_argument_parser(subparsers)


command_opt = cfg.SubCommandOpt('command',
                                title='Commands',
                                help='Available commands',
                                handler=add_command_parsers)


def main():
    import sys
    argv = sys.argv
    CONF.register_cli_opt(command_opt)
    CONF.register_opts(common_opts)
    CONF.register_opts(conductor_opts, 'conductor')
    CONF(args=argv[1:],
         project='conductor-manager',
         version="0.0.1",
         usage='%(prog)s [' + '|'.join([cmd.name for cmd in CMDS]) + ']',
         default_config_files=["/etc/cm.conf"])
    url = os.environ.get("CONDUCTOR_SERVER_URL")
    if url is not None and url != "":
        CONF.conductor.server_url = url
    try:
        CONF.command.cmd_class.main()
    except Exception as e:
        err_msg = str(e)
        if err_msg is None or err_msg == "":
            print("empty error message")
        else:
            print(err_msg)


if __name__ == '__main__':
    main()
