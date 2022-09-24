#!/bin/bash

DIR=$PWD/../
NAME='venv'

python -m venv $DIR/target/$NAME

source $DIR/target/$NAME/bin/activate
OUT=$(which python)
PYBINARY=echo "${OUT}"
OUT=$(python --version)
PYVERSION=echo "${OUT}"
OUT=$(python -c $(echo "$PYBINARY.split('bin')[0]+'lib/python{}.{}/'.format($PYVERSION.split('.')[0], $PYVERSION.split('.')[1])") )
PYDIR=echo "${OUT}"
cp $DIR/src/main/python/*.py $PYDIR/site-packages/
python -m pip install --upgrade pip
python -m pip install tk
python -m pip install untangle
deactivate
