#!/usr/bin/env bash

rm -rf bin include lib *.egg-info .Python pip-selfcheck.json share
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

