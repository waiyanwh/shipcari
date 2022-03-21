FROM ubuntu:18.04
LABEL maintainer="chrisanhvo@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev poppler-utils

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 80
CMD [ "python3", "-u", "app.py" ]
