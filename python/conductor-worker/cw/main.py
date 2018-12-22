import os
from oslo_config import cfg
from condu import Condu
from cw.db import get_db_api
from oslo_utils import importutils


CONF = cfg.CONF

database_opts = [
    cfg.StrOpt('sql_connection',
               default="mysql://root:123@ali:3306/db_test",
               help='sql_connection'),
]

conductor_opts = [
    cfg.StrOpt('server_url',
               default="http://tx2:8080/api",
               help='Conductor server url..'
               ),
]

all_workers = ['worker1']


def put_all_tasks(cw):
    for worker in all_workers:
        worker_module = importutils.import_module("cw.worker.{}".format(worker))
        for n, t in worker_module.tasks.items():
            cw.put_task(n, t)


def main():
    import sys
    argv = sys.argv
    CONF.register_opts(database_opts, 'database')
    CONF.register_opts(conductor_opts, 'conductor')
    CONF(args=argv[1:],
         project='conductor-worker',
         version="0.0.1",
         default_config_files=["/etc/cw.conf"])
    url = os.environ.get("CONDUCTOR_SERVER_URL")
    if url is not None and url != "":
        CONF.conductor.server_url = url

    options = dict(
        sql_connection=CONF.database.sql_connection,
        opts={}
    )
    get_db_api().configure_db(options)

    cw = Condu(CONF.conductor.server_url)
    put_all_tasks(cw)
    print("start tasks: %s" % str(cw.tasks.keys()))
    cw.start_tasks(polling_interval=0.1, processes=5)


if __name__ == '__main__':
    main()
