

class BaseApp(object):

    name = None

    @classmethod
    def add_argument_parser(cls, subpasers):
        parser = subpasers.add_parser(cls.name, help=cls.__doc__)
        parser.set_defaults(cmd_class=cls)
        return parser
