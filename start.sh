#!/usr/bin/env sh


export PYTHONPATH=lib
export LD_LIBRARY_PATH=lib

python manage.py $@
