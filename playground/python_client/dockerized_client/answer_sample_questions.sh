#!/bin/bash

# safely execute this bash

# e => exit on the first failure
# x => all executed commands are printed to the terminal
# u => unset variables are erros
# a => export all variables to the environment
# E => any trap on ERR is inherited by the shell functions
# -o pipefail => produces a failure code if any stage fails

# Set bash options for safety and verbosity
set -Eeuoxa pipefail

# Get the directory of the script
LOCAL_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Make the build_image.sh script executable
chmod a+x $LOCAL_DIRECTORY/scripts/build_image.sh

#build the container
$LOCAL_DIRECTORY/scripts/build_image.sh

# Run the docker container with volume mapping and interactive mode
docker run -v $LOCAL_DIRECTORY/../data:/app/python-client/data -it python-client:latest $@