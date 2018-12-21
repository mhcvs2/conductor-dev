from workers.lib.common import debug


@debug
def put_metadata(task):
    input_data = task["inputData"]
    metadata_script = input_data['metadata_script']
    random_number = input_data['random_number']
    split_name = metadata_script.rstrip('.py').split('_')
    cluster_id = '{}{}{}'.format(split_name[-2],
                                 split_name[-1],
                                 str(random_number))
    cmd = 'python %s %s' % (metadata_script, cluster_id)
    task["output"] = dict(cluster_id=cluster_id)
    return task, cmd
