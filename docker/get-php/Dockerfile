FROM tutum/apache-php
MAINTAINER Mikael Kall <kall.micke@gmail.com>

EXPOSE 80

RUN apt-get update && apt-get install -y \
    python \
    python-pyside \
    python-pip \
    python3-pip 

ADD app/index.php /app/index.php
