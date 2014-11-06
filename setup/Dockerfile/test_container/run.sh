#!/bin/bash

CNAME='koide/test'
docker build -t $CNAME .
docker run -d -p 22 -p 80 $CNAME
