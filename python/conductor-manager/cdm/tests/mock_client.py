

class MockClient(object):

    def __init__(self, *args, **kwargs):
        print("init mock client-----")
        self.print_paras(*args, **kwargs)

    def print_paras(self, *args, **kwargs):
        if len(args) > 0:
            print("args: %s" % str(args))
        if len(kwargs) > 0:
            print("kwargs: %s" % str(kwargs))

    def get_mock_method(self, name):
        def mock_method(*args, **kwargs):
            print("method name: %s ---------" % name)
            self.print_paras(*args, **kwargs)
        return mock_method

    def __getattr__(self, item):
        return self.get_mock_method(item)


if __name__ == '__main__':
    c = MockClient()
    c.do1("hah")
