# placeholder:
#  IMAGE, USERNAME, PORTS, ID_RSA_PUB, BUILD_TIME
# images(20141127):
#  admin/apache2, admin/jenkins
FROM admin/jenkins:ubuntu1404

MAINTAINER koide

# Setting root
RUN echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBbnP2Va1126LCsDUjrJ8+wdGLYsJRZkcKKXr12seAcAjlaRZWJ6W93Dzx6RGrjoLV4PAiGvDi9UD35Duvkbx02AKjUAZUkl7JiEDrGyC70ekqouejAmVnZzadyBVI1SXqw37qXTJYBsVn6QiIVhByAAgaMy40ORZm5fVmtpL2mNodKPHoKWOxlwJW3OYNfn6RS52JoQASrXyIirV97O9yAcMTUQC7D7oxQFyLdaUUzJjQ7h1dvXkjCF2yLA9Rry7yLQutFNrT5ZsJFJemLZWCeOGgCUliCfGjHmAZV9dbk8nK76bY2r/1k3jT0hnJi9059hQlG6ABgvY3xDRzqYD3 yano@yano-ubuntu > /tmp/your_key
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

EXPOSE  82 24
CMD ['/sbin/my_init']
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN echo '2014-11-29 19:01:12'
