FROM ubuntu:latest
MAINTAINER liraop <pedrolira@live.com>

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY ./app/requirements.txt /tmp/requirements.txt
RUN pip3 install -qr /tmp/requirements.txt

RUN mkdir -p /var/app/
COPY ./app /var/app/

EXPOSE 5000
WORKDIR /var/app


CMD ["python3", "./ldapy.py"]
