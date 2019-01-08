import os
import sys
from oslo_config import cfg


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

log_opts = [
    cfg.StrOpt('level',
               default="info",
               help='log level NOTSET/DEBUG/INFO/WARNING/ERROR/CRITICAL'
               ),
]


def init_config():
    argv = sys.argv
    CONF.register_opts(database_opts, 'database')
    CONF.register_opts(conductor_opts, 'conductor')
    CONF.register_opts(log_opts, 'log')
    CONF(args=argv[1:],
         project='conductor-worker',
         version="0.0.1",
         default_config_files=["/etc/cw.conf"])
    url = os.environ.get("CONDUCTOR_SERVER_URL")
    if url is not None and url != "":
        CONF.conductor.server_url = url
