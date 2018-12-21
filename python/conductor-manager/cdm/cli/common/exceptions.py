
class BaseException(Exception):

    def __init__(self, message):
        self.message = message
        super(BaseException, self).__init__(self.message)

    def __str__(self):
        return self.message


class JsonFormatError(BaseException):

    def __init__(self, e):
        self.message = "json format error: {}".format(str(e))
        super(JsonFormatError, self).__init__(self.message)


class MissFieldError(BaseException):

    def __init__(self, field_name, file_path):
        self.message = "missing field '{}'(path={})".format(field_name, file_path)
        super(MissFieldError, self).__init__(self.message)
