from cw.db.data_models.test1 import DBUser


def mhc1(task):
    user = DBUser.get_by(id=2)
    task.status = 'COMPLETED'
    task.outputData = {'name': user.name}
    task.append_to_logs('worked nice')


def mhc2(task):
    user = DBUser.get_by(id=2)
    user.name = "new-name"
    user.save()
    task.status = 'COMPLETED'
    task.outputData = {'name': user.name}
    task.append_to_logs('worked nice')
