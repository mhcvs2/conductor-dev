import os
import sys
import logging
import subprocess
from functools import wraps


log = logging.getLogger('WORKER')


def init_log():
    formatter = logging.Formatter('%(levelname)s: - %(message)s')
    console = logging.StreamHandler(sys.stdout)
    log.setLevel(logging.getLevelName(
                        os.environ.get('WORKER_LOG_LEVEL', 'INFO')))
    console.setFormatter(formatter)
    log.addHandler(console)

init_log()


def debug(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        name = fn.__name__
        log.debug('%s start', name)
        try:
            out = apply(fn, args, kwargs)
            if isinstance(out, tuple) and len(out) > 1:
                if len(out) > 2:
                    env = out[2]
                else:
                    env = os.environ
                try:
                    if isinstance(out[1], list):
                        output = run_commands(out[1], env)
                    else:
                        output = run_command(out[1], env)
                except ShellException as ex:
                    out = out[0]
                    out["status"] = "FAILED"
                    out["output"] = {"logs": {"error": '{}: {}'.format(ex.__class__.__name__,
                                                                       str(ex))}}
                else:
                    out = out[0]
                    out["status"] = "COMPLETED"
                    if 'output' in out:
                        out["output"].update({"logs": {"stdout": output}})
                    else:
                        out["output"] = {"logs": {"stdout": output}}
        except ValueError as e:
            out = args[0]
            out["status"] = "FAILED"
            out["output"] = {"logs": {"error": '{}: {}'.format(e.__class__.__name__,
                                                               e.message)}}
        log.debug('taskId: %s', out['taskId'])
        log.debug('workerId: %s', out['workerId'])
        if 'output' in out:
            log.debug('output: %s', out['output'])
        else:
            out['output'] = {}
        log.debug('%s end', name)
        out["status"] = "COMPLETED"
        return out
    return wrapper


class ShellException(Exception):

    def __init__(self, code, stdout='', stderr=''):
        self.code = code
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return 'exit code %d - %s' % (self.code, self.stderr)


def run_command(command, env=os.environ):
    log.debug('Run cmd: %s' % command)
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            env=env,
                            shell=True)
    proc.wait()

    stdout, stderr = proc.communicate()
    if proc.returncode > 0:
        raise ShellException(proc.returncode, stdout.strip(), stderr.strip())

    return stdout.strip()


def run_commands(commands, env=os.environ):
    for command in commands:
        run_command(command, env)
    return 'success'


def get_input_value(task, key, default=''):
    input_data = task["inputData"]
    if key in input_data and input_data[key]:
        return input_data[key]
    return default

