

def test_task(task):
    input_data = task["inputData"]
    task["status"] = "COMPLETED"
    task["output"] = dict(primaryIp='00000',
                         logs='receive inputData: %s' % input_data)
    return task
