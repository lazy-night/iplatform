# placeholder:
#  IMAGE, USERNAME, PORTS, ID_RSA_PUB, BUILD_TIME
# images(20141127):
#  admin/apache2, admin/jenkins
FROM admin/apache2:ubuntu1404

MAINTAINER koide

# Setting root
RUN echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDeCW+ZRJzU7Mh+dcvW3RZVMh7FDX15owZaKx/TtM3arztwjnYEh8es8Eg2VFiMMM5otE/sJRqqbXoOJaHvXbHU+V5XjBKJpPBMbH56n1Od6KkaOPywaSwmhgXkz/ElMIdQypBH7U1Ecwj4AKoawP/IwMPW3+TnkGbEeXFrvIB3W3hLiBZFUqnraxGKUh9kNsvUa4Y/ZwC5wSEkRCtYQnZ7u384LpPnLk3R7LVowVBj0KzM/AzANtRbqXxfP7GjS4e2xskbWcTOn5ESGQWciQAOtnQgrPELhrJYl1ruEINeckAHgeZOwhSiwGxkMfWvPAu3mMgCuHxPIC/dOLWZLruH > /tmp/your_key
RUN cat /tmp/your_key >> /root/.ssh/authorized_keys && \
    chmod 600 /root/.ssh/authorized_keys

# Add user
RUN adduser --disabled-password --gecos '' test
RUN mkdir -m 700 /home/test/.ssh && \
    chown test:test /home/test/.ssh
RUN cat /tmp/your_key >> /home/test/.ssh/authorized_keys && \
    chmod 600 /home/test/.ssh/authorized_keys && \
    rm -f /tmp/your_key
RUN echo 'test ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    echo 'test:test' | chpasswd
RUN chown -R test:test /home/test/

EXPOSE 22  22 80 8080
CMD ['/sbin/my_init']
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN echo '2014-11-27 08:14:24'
