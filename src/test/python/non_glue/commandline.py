import subprocess

def communicate(cmd):
    if type(cmd)==type([]):
        pass
    elif type(cmd)==type(''):
        cmd=[cmd]
    else:
        cmd=['echo', 'command not executed']
    P=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = P.communicate()
    return {'in':cmd, 'out':stdout.decode("utf-8"), 'err':stderr}