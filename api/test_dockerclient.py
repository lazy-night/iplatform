import pytest
import unittest
import dockerclient


class TestDockerClient(unittest.TestCase):

    def setUp(self):
        self.dockerc = dockerclient.DockerClient()


    def test_containers(self):
        print '[TestDockerClient.test_containers()]'
        print '[self.dockerc.containers()]' + str(self.dockerc.containers())
        assert len(self.dockerc.containers(name='koide')) == 0


    def test_images(self):
        print '[TestDockerClient.test_images()]'
        print '[self.dockerc.images()]' + str(self.dockerc.images())
        assert len(self.dockerc.images(name='koide')) > 0


    def test_build(self):
        print '[TestDockerClient.test_build()]'
        result = self.dockerc.build(
            image='ubuntu:14.04', app='apache2', port=[80],
            id_rsa_pub='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDeCW+ZRJzU7Mh+dcvW3RZVMh7FDX15owZaKx/TtM3arztwjnYEh8es8Eg2VFiMMM5otE/sJRqqbXoOJaHvXbHU+V5XjBKJpPBMbH56n1Od6KkaOPywaSwmhgXkz/ElMIdQypBH7U1Ecwj4AKoawP/IwMPW3+TnkGbEeXFrvIB3W3hLiBZFUqnraxGKUh9kNsvUa4Y/ZwC5wSEkRCtYQnZ7u384LpPnLk3R7LVowVBj0KzM/AzANtRbqXxfP7GjS4e2xskbWcTOn5ESGQWciQAOtnQgrPELhrJYl1ruEINeckAHgeZOwhSiwGxkMfWvPAu3mMgCuHxPIC/dOLWZLruH',
            tag='koide/test_apache2')
        assert len(self.dockerc.images(name='koide')) > 2


    def test_create_container(self):
        print '[TestDockerClient.test_create_container()]'
        image = 'koide/test_apache2'
        ports = [80]
        result = self.dockerc.create_container(image=image, ports=ports)
        assert len(self.dockerc.containers(name='koide', all=True)) > 0


    def test_create_container_error_of_not_image(self):
        print '[TestDockerClient.test_create_container()]'
        image = 'koide/error'
        ports = [80]
        result = self.dockerc.create_container(image=image, ports=ports)
        assert result == None


    def test_start(self):
        print '[TestDockerClient.test_start()]'
        tag = 'koide/test_apache2'
        res = self.dockerc.build(image='ubuntu:14.04', app='apache2', port=[80],
            id_rsa_pub='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDeCW+ZRJzU7Mh+dcvW3RZVMh7FDX15owZaKx/TtM3arztwjnYEh8es8Eg2VFiMMM5otE/sJRqqbXoOJaHvXbHU+V5XjBKJpPBMbH56n1Od6KkaOPywaSwmhgXkz/ElMIdQypBH7U1Ecwj4AKoawP/IwMPW3+TnkGbEeXFrvIB3W3hLiBZFUqnraxGKUh9kNsvUa4Y/ZwC5wSEkRCtYQnZ7u384LpPnLk3R7LVowVBj0KzM/AzANtRbqXxfP7GjS4e2xskbWcTOn5ESGQWciQAOtnQgrPELhrJYl1ruEINeckAHgeZOwhSiwGxkMfWvPAu3mMgCuHxPIC/dOLWZLruH', tag=tag)
        ports = [80]
        container = self.dockerc.create_container(image=tag, ports=ports)
        port_bindings={80 : None}
        self.dockerc.start(container=container, port_bindings=port_bindings)
        assert len(self.dockerc.containers(name='koide')) > 0


    def test_stop(self):
        print '[TestDockerClient.test_stop()]'
        tag = 'koide/test_apache2'
        res = self.dockerc.build(image='ubuntu:14.04', app='apache2', port=[80],
            id_rsa_pub='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDeCW+ZRJzU7Mh+dcvW3RZVMh7FDX15owZaKx/TtM3arztwjnYEh8es8Eg2VFiMMM5otE/sJRqqbXoOJaHvXbHU+V5XjBKJpPBMbH56n1Od6KkaOPywaSwmhgXkz/ElMIdQypBH7U1Ecwj4AKoawP/IwMPW3+TnkGbEeXFrvIB3W3hLiBZFUqnraxGKUh9kNsvUa4Y/ZwC5wSEkRCtYQnZ7u384LpPnLk3R7LVowVBj0KzM/AzANtRbqXxfP7GjS4e2xskbWcTOn5ESGQWciQAOtnQgrPELhrJYl1ruEINeckAHgeZOwhSiwGxkMfWvPAu3mMgCuHxPIC/dOLWZLruH',
            tag=tag)
        ports = [80]
        container = self.dockerc.create_container(image=tag, ports=ports)
        port_bindings={80 : None}
        self.dockerc.start(container=container, port_bindings=port_bindings)
        before = len(self.dockerc.containers(name='koide'))
        self.dockerc.stop(container=container)
        after = len(self.dockerc.containers(name='koide'))
        assert  before != after


    def test_remove_container(self):
        print '[TestDockerClient.test_remove_container()]'
        tag = 'koide/test_apache2'
        res = self.dockerc.build(image='ubuntu:14.04', app='apache2', port=[80],
            id_rsa_pub='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDeCW+ZRJzU7Mh+dcvW3RZVMh7FDX15owZaKx/TtM3arztwjnYEh8es8Eg2VFiMMM5otE/sJRqqbXoOJaHvXbHU+V5XjBKJpPBMbH56n1Od6KkaOPywaSwmhgXkz/ElMIdQypBH7U1Ecwj4AKoawP/IwMPW3+TnkGbEeXFrvIB3W3hLiBZFUqnraxGKUh9kNsvUa4Y/ZwC5wSEkRCtYQnZ7u384LpPnLk3R7LVowVBj0KzM/AzANtRbqXxfP7GjS4e2xskbWcTOn5ESGQWciQAOtnQgrPELhrJYl1ruEINeckAHgeZOwhSiwGxkMfWvPAu3mMgCuHxPIC/dOLWZLruH',
            tag=tag)
        ports = [80]
        container = self.dockerc.create_container(image=tag, ports=ports)
        port_bindings={80 : None}
        self.dockerc.start(container=container, port_bindings=port_bindings)
        self.dockerc.stop(container=container)
        before = len(self.dockerc.containers(all=True))
        self.dockerc.remove_container(container=container)
        after = len(self.dockerc.containers(all=True))
        assert  before != after


    def test_remove_image(self):
        print '[TestDockerClient.test_remove_image()]'
        print '[TODO]'
        assert True


    def tearDown(self):
        print '[TODO]'
        # kill and remove containers
