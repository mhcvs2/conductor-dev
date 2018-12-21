import random
from workers.lib.common import debug


@debug
def gen_random_number(task):
    task["status"] = "COMPLETED"
    task["output"] = dict(random_number=int(random.random() * 1000))
    return task
