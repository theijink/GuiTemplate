import os
import sys
from time import sleep

DIR=os.getcwd().split('src')[0]
NAME='venv'

def create_venv():
    path, dirs, files = next(os.walk(DIR+'target/'))
    if NAME in dirs:
        os.system('rm -rf {}'.format(DIR+"target/"+NAME))
    os.system('python -m venv {}'.format(DIR+"target/"+NAME))
    activate_venv()


def activate_venv():
    os.system("source {}/bin/activate".format(DIR+'target/'+NAME))

def install_packages():
    activate_venv()
    PYBINARY=sys.executable#str(os.system(r'echo $(python -c "import sys; print(sys.executable)")'))
    PYVERSION=sys.version.split(' ')[0]#str(os.system(r'echo $(python -c "import sys; print(sys.version.split(' ')[0])")'))
    #print('************************\nbinary: {}, version: {}\n************************'.format(PYBINARY, PYVERSION))
    PYDIR=PYBINARY.split('bin')[0]+'lib/python{}.{}/'.format(PYVERSION.split('.')[0], PYVERSION.split('.')[1])
    os.system("python -m pip install --upgrade pip")
    os.system("cp {}/src/main/python/*.py {}site-packages/".format(DIR, PYDIR))
    os.system("cp -r {}/src/test/python/non_glue {}site-packages/".format(DIR, PYDIR))
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install tk")
    os.system("python -m pip install untangle")
    os.system("python -m pip install behave")
    deactivate_venv()

def deactivate_venv():
    os.system("unset -f deactivate")

def remove_venv():
    os.system("rm -rf {}".format(DIR+'target/'+NAME))

def create_file():
    os.system("touch {}".format(DIR+'target/'+NAME+'/lib/GuiTemplate.py'))


if __name__=="__main__":
    #create_venv()
    install_packages()
    #deactivate_venv()


    ## eventually, the following steps should be taken by this (or another) script when executed by maven
    ## OPT: use makefile in between maven and python
    ## 1. create virtual environment and load dependencies (compile lifecycle)
    ## 2. perform availability tests (compile lifecycle)
    ## 3. use the code in the virtual environment to build the application according to the configuration.xml (install lifecycle)
    ## 4. perform functional tests on the application (install lifecycle)

