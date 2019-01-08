from oslo_config import cfg
from cw.common.cfg import init_config
from cw.db import get_db_api
from oslo_utils import importutils


CONF = cfg.CONF

all_workers = ['worker1']


def put_all_tasks(cw):
    for worker in all_workers:
        worker_module = importutils.import_module("cw.worker.{}".format(worker))
        for n, t in worker_module.tasks.items():
            cw.put_task(n, t)


def main():
    init_config()
    options = dict(
        sql_connection=CONF.database.sql_connection,
        opts={}
    )
    get_db_api().configure_db(options)
    from cw.condu.condu import Condu
    cw = Condu(CONF.conductor.server_url)
    put_all_tasks(cw)
    print("start tasks: %s" % str(cw.tasks.keys()))
    cw.start_tasks(polling_interval=0.1, processes=5)


if __name__ == '__main__':
    main()
