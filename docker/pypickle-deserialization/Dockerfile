FROM python:2.7-alpine

RUN set -x \
  && apk update \
  && apk add \
  vim \
  curl \
  netcat-openbsd

copy ./simpsons /opt/simpsons
WORKDIR /opt/simpsons

RUN pip install -r requirements.txt
ENTRYPOINT ["python2", "/opt/simpsons/__init__.py"]
