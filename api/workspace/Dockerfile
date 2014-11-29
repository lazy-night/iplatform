# placeholder:
#  IMAGE, USERNAME, PORTS, ID_RSA_PUB, BUILD_TIME
# images(20141127):
#  admin/apache2, admin/jenkins
FROM admin/apache2:ubuntu1404

MAINTAINER koide

# Setting root
RUN echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCRXz9Bdi3lCDzgT2dASg/b22caVDPB7xeGhP16n4kNE2RahlW6fFchHka/fP7V7ZHFZInyqYRcXETKb2GNICv9bSwcmMWuzu1CVy20yEYwyG60CVEAt07T6HP29A07RtrKlWxaAxQMc1r+lJkMzQFHnjPb4jrDNZKko1uykAzZ10xwAp/4i3094eQl605J/EMJ2uP8uKZ2l9HuKRwoaqRP0gxqQC2kBoasiZG1MLEvlmZvtWS6KYhvJx10XsxoWltddI4YMTHE8gp5+tGkJ697z5Fa0PRLY3nlSbQUcivBCv4ejNgnMpcxj0W1+OjXs33swf5imUB83D3SV+SikRNV yano@pc-kusube.ipl.office > /tmp/your_key
RUN cat /tmp/your_key >> /root/.ssh/authorized_keys && \
    chmod 600 /root/.ssh/authorized_keys

# Add user
RUN adduser --disabled-password --gecos '' yano
RUN mkdir -m 700 /home/yano/.ssh && \
    chown yano:yano /home/yano/.ssh
RUN cat /tmp/your_key >> /home/yano/.ssh/authorized_keys && \
    chmod 600 /home/yano/.ssh/authorized_keys && \
    rm -f /tmp/your_key
RUN echo 'yano ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    echo 'yano:yano' | chpasswd
RUN chown -R yano:yano /home/yano/

EXPOSE  22 80
CMD ['/sbin/my_init']
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN echo '2014-11-28 02:57:13'
