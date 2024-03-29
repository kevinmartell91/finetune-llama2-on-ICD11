#!/bin/bash

# safely execute this bash
# e => exit on the first failure
# x => all executed commands are printed to the terminal
# u => unset variables are erros
# a => export all variables to the environment
# E => any trap on ERR is inherited by the shell functions
# -o pipefail => produces a failure code if any stage fails

# set bash options for safety and verbosity
set -Eeuoxa pipefail

# get the directory of this scrip
LOCAL_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Set PYTHON_PATH variable to the parent directory of the script
# This step is necessary to ensure that the correct Python interpreter 
# is used for running the app
PYTHONPATH="$LOCAL_DIRECTORY/.." python3 $LOCAL_DIRECTORY/../slack/app.py