from cw.worker.worker1.common import LOG
from cw.db.data_models.test1 import DBUser
from cw.common.task import Status


def task_1(task):
    LOG.debug("task_1 run")
    user = DBUser.get_by(id=2)
    task.status = Status.COMPLETED
    task.outputData = {'name': user.name}
    task.append_to_logs('worked nice')
    LOG.info('worked nice')


def task_5(task):
    user = DBUser.get_by(id=2)
    user.name = "new-name"
    user.save()
    task.status = Status.COMPLETED
    task.outputData = {'name': user.name}
    task.append_to_logs('worked nice')
