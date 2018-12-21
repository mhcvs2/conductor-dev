

class DockerCompose(object):

    def __init__(self, file_path, project_name):
        self.cmd = 'docker-compose'
        self.file_path = file_path
        self.project_name = project_name

    @property
    def base_cmd(self):
        return '%(cmd)s -f %(file_path)s -p %(project_name)s ' % dict(
            cmd=self.cmd,
            file_path=self.file_path,
            project_name=self.project_name,
        )

    def get_scale_cmd(self, service_name, number):
        return '{} scale {}={}'.format(self.base_cmd,
                                       service_name,
                                       str(number))

    @property
    def stop_cmd(self):
        return '{} stop'.format(self.base_cmd)

    @property
    def rm_cmd(self):
        return '{} rm -f'.format(self.base_cmd)
