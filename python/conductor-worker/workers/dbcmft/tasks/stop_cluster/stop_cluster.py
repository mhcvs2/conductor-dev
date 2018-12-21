from workers.lib.common import debug
from workers.lib.compose import DockerCompose
from workers.lib.docker import get_image


@debug
def stop_cluster(task):
    input_data = task["inputData"]
    cluster_id = input_data['cluster_id']
    image = get_image(cluster_id)
    compose_file = input_data['compose_file']
    dc = DockerCompose(compose_file, cluster_id)
    env = dict(
        image=image,
        CLUSTER_ID=cluster_id,
        CONSUL='109.105.4.65'
    )
    return task, dc.stop_cmd, env
