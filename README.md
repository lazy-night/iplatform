IPLatform
====

This application is a PaaS. Use the docker, you can build a server environment without an engineer. 

## Description

## Demo

## VS. 

## Requirement

[requirements.txt](https://github.com/lazy-night/iplatform/blob/master/requirements.txt)

## Usage

# How to run server
    $ cd api/Dockerfile/ubuntu14.04/base
    $ docker build -t admin/base:ubuntu1404 .
    $ cd api/Dockerfile/ubuntu14.04/apache2
    $ docker build -t admin/apache2:ubuntu1404 .
    $ cd api/Dockerfile/ubuntu14.04/jenkins
    $ docker build -t admin/jenkins:ubuntu1404 .
    $ pip install -r requirements.txt
    $ python run.py

## Install

## Contribution

## Document

## Ticket

## Deploy

## Test

## Environment
```sh
# cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=14.04
DISTRIB_CODENAME=trusty
DISTRIB_DESCRIPTION="Ubuntu 14.04.1 LTS"
```

```sh
# uname -a
Linux iplatform 3.13.0-32-generic #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
```

```sh
# docker version
Client version: 1.3.1
Client API version: 1.15
Go version (client): go1.3.3
Git commit (client): 4e9bbfa
OS/Arch (client): linux/amd64
Server version: 1.3.1
Server API version: 1.15
Go version (server): go1.3.3
Git commit (server): 4e9bbfa
```

## Licence

[MIT]

## Author

[yymm](https://github.com/yymm)

[doragon](https://github.com/doragon)
