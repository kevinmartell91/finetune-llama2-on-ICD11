#!/bin/bash

# safely execute this bash

# e => exit on the first failure
# x => all executed commands are printed to the terminal
# u => unset variables are erros
# a => export all variables to the environment
# E => anytrap on ERR is inherited by the shell functions
# -o pipefail => produces a failure code if any stage fails

# set bash option for safety and verbosity
set -Eeuoxa pipefail

# get the directory of this scrip
LOCAL_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Build the Docker image for the Python client
docker build -t python-client:latest -f $LOCAL_DIRECTORY/../Dockerfile $LOCAL_DIRECTORY/../..