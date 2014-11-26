FROM phusion/baseimage:0.9.15

MAINTAINER koide

RUN apt-get -y update

ENV HOME /root
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ['/sbin/my_init']
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
