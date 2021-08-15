FROM ubuntu:18.04

LABEL maintainer="chrisanhvo@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev poppler-utils

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

# ENTRYPOINT [ "python3" ]

CMD [ "python3", "-u", "app.py" ]
