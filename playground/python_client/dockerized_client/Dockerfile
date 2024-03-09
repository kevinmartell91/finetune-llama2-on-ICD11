FROM python:3.11 as base

ARG PACKAGE_NAME="python-client"

# Install Ubuntu libraries
RUN apt-get -yq update

# Install python packages
WORKDIR /app/${PACKAGE_NAME}

COPY ./requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all files to the container
COPY ./dockerized_client/scripts /app/${PACKAGE_NAME}/scripts
COPY ./answer_sample_questions.py /app/${PACKAGE_NAME}/answer_sample_questions.py
COPY ./sample_questions.jsonl /app/${PACKAGE_NAME}/sample_questions.jsonl

WORKDIR /app/${PACKAGE_NAME}

# Make the start-python-client.sh script executable
RUN chmod a+x /app/${PACKAGE_NAME}/scripts/start_python_client.sh

ENV PACKAGE_NAME=$PACKAGE_NAME
RUN echo "BRIAN"
# Set the entrypoint to start the python client
ENTRYPOINT ["/app/python-client/scripts/start_python_client.sh"]