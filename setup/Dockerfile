FROM ubuntu:13.10

MAINTAINER doragon

# timezone
RUN echo "Asia/Tokyo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

# install
RUN apt-get update && apt-get clean
RUN apt-get -y install wget vim python-pip curl

###### jenkins start ######
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt-key update
RUN apt-get update && apt-get clean
RUN apt-get install -y jenkins
 
RUN mkdir /data
ADD ./conf/jenkins_plugin.sh /data/jenkins_plugin.sh
###### jenkins end ######

###### ssh start ######
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update && apt-get clean
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo "root:root" |chpasswd
###### ssh end ######

###### test modules start ######
RUN pip install -U pytest
RUN pip install pytest-pep8 pytest-cov docker-py pylint
RUN apt-get install -y sloccount
RUN easy_install -U clonedigger
###### test modules end ######

EXPOSE 22 8080
CMD ["/bin/bash", "-c", "service jenkins start; /usr/sbin/sshd -D"]
