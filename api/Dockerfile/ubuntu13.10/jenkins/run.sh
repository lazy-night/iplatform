#!/bin/bash
 
docker build -t admin/jenkins .
docker run -d -p 22 -p 8080 admin/jenkins
