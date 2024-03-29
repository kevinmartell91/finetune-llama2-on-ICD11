FROM python:3.11-slim

ARG PAKAGE_NAME="slack-client"

# Install Ubuntu libraries
RUN apt-get -yq update 

# Install pyhton packages
WORKDIR /app/${PAKAGE_NAME}

COPY ./requirements.txt /app/${PAKAGE_NAME}/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all files to the container
COPY . /app/${PAKAGE_NAME}

WORKDIR /app/${PAKAGE_NAME}

RUN chmod a+x /app/${PAKAGE_NAME}/scripts/start-slack-client.sh

ENTRYPOINT /app/slack-client/scripts/start-slack-client.sh