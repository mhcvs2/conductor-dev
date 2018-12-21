from workers.lib.common import debug
from workers.lib.consul_client import Consul


@debug
def consul_put_kv(task):
    input_data = task["inputData"]
    ip = input_data['ip']
    key = input_data['key']
    value = input_data['value']
    c = Consul(host=ip)
    c.put(key, value)
    task["status"] = "COMPLETED"
    return task
