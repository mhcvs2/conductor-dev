from cdm.cli.common.exceptions import *


def check_field(field_name, data, file_path=""):
    if field_name not in data:
        raise MissFieldError(field_name, file_path)


def start_with(s, sub):
    if sub not in s:
        return False
    elif s.index(sub) != 0:
        return False
    else:
        return True
