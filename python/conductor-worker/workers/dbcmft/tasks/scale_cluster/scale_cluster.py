from workers.lib.common import debug
from workers.lib.compose import DockerCompose
from workers.lib.docker import get_image


@debug
def scale_cluster(task):
    input_data = task["inputData"]
    cluster_id = input_data['cluster_id']
    service_name = input_data['service_name']
    compose_file = input_data['compose_file']
    number = input_data['number']
    if 'image' in input_data and input_data['image']:
        image = input_data['image']
    else:
        image = get_image(cluster_id)
    if 'project_name' in input_data and input_data['project_name']:
        project_name = input_data['project_name']
    else:
        project_name = cluster_id
    if 'datacenter' in input_data and input_data['datacenter']:
        datacenter = input_data['datacenter']
    else:
        datacenter = 'default'
    dc = DockerCompose(compose_file, project_name)
    env = dict(
        image=image,
        CLUSTER_ID=cluster_id,
        CONSUL='109.105.4.65',
        DATACENTER=datacenter
    )
    return task, dc.get_scale_cmd(service_name, number), env
