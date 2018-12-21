from workers.lib.common import debug, get_input_value, log
from workers.lib.consul_client import Consul


@debug
def consul_clear_service(task):
    ip = get_input_value(task, 'ip', '109.105.4.65')
    c = Consul(host=ip)
    result = []
    all_service_name = c.get_all_service_name()
    for name in all_service_name:
        result.extend(c.deregister_checks_services(name=name))
    task['output'] = dict(clear_services=result)
    log.info('Clear service: %s', str(result))
    return task
