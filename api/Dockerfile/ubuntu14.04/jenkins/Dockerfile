FROM admin/base:ubuntu1404

MAINTAINER koide

RUN apt-get -y update
RUN apt-get -y install wget

RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt-key update
RUN apt-get -y update && apt-get clean
RUN apt-get install -y jenkins

EXPOSE 22 8080
CMD ['/sbin/my_init']
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
