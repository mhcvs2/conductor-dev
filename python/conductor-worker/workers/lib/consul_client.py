import time
import consul as pyconsul
from workers.lib.common import log


class Consul(object):
    """ Consul represents the Consul instance this node talks to """

    def __init__(self, host='109.105.4.65'):
        self.client = pyconsul.Consul(host=host)

    def get(self, key):
        """
        Return the Value field for a given Consul key.
        Handles None results safely but lets all other exceptions
        just bubble up.
        """
        result = self.client.kv.get(key)
        if result[1]:
            return result[1]['Value']
        return None

    def put(self, key, value):
        """ Puts a value for the key; allows all exceptions to bubble up """
        return self.client.kv.put(key, value)

    def delete(self, key):
        log.debug('Delete key: %s' % key)
        return self.client.kv.delete(key, recurse=True)

    def get_all_service_name(self):
        all_service = set()
        services = self.client.agent.services()
        for service_id, service in services.items():
            all_service.add(service['Service'])
        return all_service

    def get_check_service_ids(self, name, timeout=10, critical=True, sid=None):
        """  get all service and check id by service name """
        check_ids = []
        service_ids = []
        while timeout > 0:
            try:
                nodes = self.client.health.service(name)[1]
                for node in nodes:
                    if sid is not None and node["Service"]["ID"] != sid:
                        continue
                    if critical:
                        if len(node["Checks"]) > 1 and node["Checks"][1]["Status"] == "critical":
                            check_ids.append(node["Checks"][1]["CheckID"])
                            service_ids.append(node["Service"]["ID"])
                    else:
                        if len(node["Checks"]) > 1:
                            check_ids.append(node["Checks"][1]["CheckID"])
                        service_ids.append(node["Service"]["ID"])
                return check_ids, service_ids
            except pyconsul.ConsulException:
                timeout = timeout - 1
                time.sleep(1)
                continue
            except IndexError:
                return [], []
        raise Exception('Could not get service ips before timeout.')

    def deregister_checks_services(self, name, critical=True, sid=None):
        """ deregister service and check by service name """
        critical_check, critical_service = self.get_check_service_ids(name,
                                                                      critical=critical,
                                                                      sid=sid)
        for c_id in critical_check:
            self.client.agent.check.deregister(c_id)
        for s_id in critical_service:
            self.client.agent.service.deregister(s_id)
        return critical_service

