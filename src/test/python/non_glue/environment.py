import non_glue.commandline
import os

def deactivate_and_activate_venv(venv):
    pwd=os.getcwd()+'/'
    for dir in venv.split('/'):
        path, dirs, files = next(os.walk(pwd))
        pwd+=str(dir+'/')
        assert dir in dirs, 'Directory {} not found on expected path {}'.format(dir, path)
    return non_glue.commandline.communicate(["source", "{}bin/activate".format(pwd)])

def get_python_executable():
    return non_glue.commandline.communicate(["which python"])['out']

def import_module_from_string(library_name):
    globals()[library_name]=__import__(library_name)
    return globals()[library_name]

