#!/bin/bash
 
wget -O jenkins-cli.jar http://127.0.0.1:8080/jnlpJars/jenkins-cli.jar
 
# cobertura
java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin http://updates.jenkins-ci.org/download/plugins/cobertura/1.9.5/cobertura.hpi
 
# violations
java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin http://updates.jenkins-ci.org/download/plugins/violations/0.7.11/violations.hpi
 
# sloccount
java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin http://updates.jenkins-ci.org/download/plugins/sloccount/1.19/sloccount.hpi
 
# clonedigger
java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin http://updates.jenkins-ci.org/download/plugins/htmlpublisher/1.3/htmlpublisher.hpi
 
service jenkins restart
