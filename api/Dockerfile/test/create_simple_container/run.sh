#!/bin/bash

CNAME='koide/sample_container'
docker build -t $CNAME .
docker run -d -p 22 -p 80 $CNAME
