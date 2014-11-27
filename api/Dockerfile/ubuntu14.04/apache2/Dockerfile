FROM admin/base:ubuntu1404

MAINTAINER koide

RUN apt-get -y update --fix-missing
RUN apt-get -y install apache2

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 22 80
CMD ['/sbin/my_init']
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
