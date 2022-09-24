import os
import sys

DIR=os.getcwd().split('src')[0]
NAME='venv'

def create_venv():
    os.system("python -m venv {}".format(DIR+'target/'+NAME))

def activate_venv():
    os.system("source {}/bin/activate".format(DIR+'target/'+NAME))

def install_packages():
    activate_venv()
    PYBINARY=sys.executable
    PYVERSION=sys.version.split(' ')[0]
    PYDIR=PYBINARY.split('bin')[0]+'lib/python{}.{}/'.format(PYVERSION.split('.')[0], PYVERSION.split('.')[1])
    os.system("cp {}src/main/python/*.py {}site-packages/".format(DIR, PYDIR))
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install tk")
    os.system("python -m pip install untangle")
    deactivate_venv()

def deactivate_venv():
    os.system("unset -f deactivate")

def remove_venv():
    os.system("rm -rf {}".format(DIR+'target/'+NAME))

def create_file():
    os.system("touch {}".format(DIR+'target/'+NAME+'/lib/GuiTemplate.py'))


if __name__=="__main__":
    create_venv()
    install_packages()
    #deactivate_venv()
