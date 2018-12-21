from workers.lib.common import debug, get_input_value


@debug
def test_task(task):
    value = get_input_value(task, 'key', default='haha')
    task["output"] = dict(primaryIp='00000', logs='receive inputData: %s' % value)
    return task
