import os
from oslo_config import cfg
from condu import Condu
from cw.worker.worker1.mhc1 import *


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
    cw = Condu(CONF.conductor.server_url)
    cw.put_task('mhc1', mhc1)
    cw.put_task('mhc2', mhc2)
    cw.start_tasks(polling_interval=0.1, processes=5)


if __name__ == '__main__':
    main()
