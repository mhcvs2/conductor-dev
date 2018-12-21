from cdm.cli.common.exceptions import *


def check_field(field_name, data, file_path=""):
    if field_name not in data:
        raise MissFieldError(field_name, file_path)
