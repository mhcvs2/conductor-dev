from workers.lib.common import run_command


def get_image(keyword):
    return run_command("docker ps|grep %s|awk 'NR==1 {print $2}'" % keyword)