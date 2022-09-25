import os
import sys
import subprocess

DIR=os.getcwd().split('src')[0]
NAME='venv'

def create_venv():
    cmd=["python -m venv {}".format(DIR+'target/'+NAME)]
    P=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = P.communicate()
    #return {'in':cmd, 'out':stdout.decode("utf-8"), 'err':stderr})
    print(stdout.decode('utf-8'))

def activate_venv():
    os.system("source {}/bin/activate".format(DIR+'target/'+NAME))

def deactivate_venv():
    os.system("unset -f deactivate")

def compile_packages():
    activate_venv()
    PYBINARY=sys.executable
    PYVERSION=sys.version.split(' ')[0]
    PYDIR=PYBINARY.split('bin')[0]+'lib/python{}.{}/'.format(PYVERSION.split('.')[0], PYVERSION.split('.')[1])
    os.system("cp {}src/main/python/*.py {}site-packages/".format(DIR, PYDIR))
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install tk")
    os.system("python -m pip install untangle")
    deactivate_venv()


def remove_venv():
    os.system("rm -rf {}".format(DIR+'target/'+NAME))

def create_file():
    os.system("touch {}".format(DIR+'target/'+NAME+'/lib/GuiTemplate.py'))

def build_application():
    pass

if __name__=="__main__":
    print('Busy...')
    if '-venv' in sys.argv:
        create_venv()
    if '-compile' in sys.argv:
        compile_packages()
    if '-install' in sys.argv:
        build_application()
    #install_packages()
    #deactivate_venv()
    print('\t...done!')

