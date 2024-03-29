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

# get the directory of this script
LOCAL_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Build the container
$LOCAL_DIRECTORY/scripts/build-image.sh

# Start the container
docker run -it \
    --env-file ../../.env \
    -v $LOCAL_DIRECTORY/.data:/app/slack-client/.data \
    -p 3000:3000 \
    slack-client:latest