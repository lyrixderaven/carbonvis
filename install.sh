#!/usr/bin/env bash

virtualenv -p python3 .
bin/pip install --upgrade pip setuptools

bin/pip install -e ".[testing]"
bin/initialize_carbonvis_db development.ini