import os

DIR=os.getcwd().split('src')[0]+'target/'
NAME='venv'

def setup_venv():
    os.system("python -m venv {}".format(DIR+NAME))
    os.system("source {}/bin/activate".format(DIR+NAME))

def install_packages():
    pass

def deactivate_venv():
    os.system("deactivate")

def remove_venv():
    os.system("rm -rf {}".format(DIR+NAME))


if __name__=="__main__":
    setup_venv()
    install_packages()
    deactivate_venv()
