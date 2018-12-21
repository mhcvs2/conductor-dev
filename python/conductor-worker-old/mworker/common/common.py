import os
import sys
import logging
import time
from mworker.common import config


log = logging.getLogger('WORKER_MANAGE')


def init_log():
    formatter = logging.Formatter('%(levelname)s: - %(message)s')
    console = logging.StreamHandler(sys.stdout)
    log.setLevel(logging.getLevelName(
                        os.environ.get('WORKER_MANAGE_LOG_LEVEL', 'INFO')))
    console.setFormatter(formatter)
    log.addHandler(console)

init_log()


def format_time(timestamp):
    return time.strftime(config.TIME_FORMAT, time.localtime(timestamp))


def format_time_dict(d, *keys):
    for key in keys:
        try:
            timestamp = int(d[key])
            d[key] = format_time(timestamp)
        except (TypeError, KeyError):
            pass
