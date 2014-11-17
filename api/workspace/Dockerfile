FROM ubuntu:14.04

MAINTAINER koide

RUN apt-get -y update
RUN apt-get -y install vim wget curl apache2
RUN apt-get clean

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2



EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
