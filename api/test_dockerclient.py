import pytest
import unittest
import dockerclient


class TestDockerClient(unittest.TestCase):

    def setUp(self):
        self.dockerc = dockerclient.DockerClient()
        self.image = 'ubuntu:14.04'
        self.app = 'apache2'
        self.port = [22, 80, 8080]
        self.id_rsa_pub='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDeCW+ZRJzU7Mh+dcvW3RZVMh7FDX15owZaKx/TtM3arztwjnYEh8es8Eg2VFiMMM5otE/sJRqqbXoOJaHvXbHU+V5XjBKJpPBMbH56n1Od6KkaOPywaSwmhgXkz/ElMIdQypBH7U1Ecwj4AKoawP/IwMPW3+TnkGbEeXFrvIB3W3hLiBZFUqnraxGKUh9kNsvUa4Y/ZwC5wSEkRCtYQnZ7u384LpPnLk3R7LVowVBj0KzM/AzANtRbqXxfP7GjS4e2xskbWcTOn5ESGQWciQAOtnQgrPELhrJYl1ruEINeckAHgeZOwhSiwGxkMfWvPAu3mMgCuHxPIC/dOLWZLruH'
        self.command = '/sbin/my_init'


    @pytest.mark.skipif('"skip"')
    def test_containers(self):
        print '[TestDockerClient.test_containers()]'
        print '[self.dockerc.containers()]' + str(self.dockerc.containers())
        assert len(self.dockerc.containers(name='test')) == 0


    @pytest.mark.skipif('"skip"')
    def test_images(self):
        print '[TestDockerClient.test_images()]'
        print '[self.dockerc.images()]' + str(self.dockerc.images())
        assert len(self.dockerc.images(name='test')) > 0


    @pytest.mark.skipif('"skip"')
    def test_build(self):
        print '[TestDockerClient.test_build()]'
        tag = 'test/test_build_apache2'
        result = self.dockerc.build(
            image=self.image,
            app=self.app,
            port=self.port,
            id_rsa_pub=self.id_rsa_pub,
            tag=tag
        )
        images = self.dockerc.images(name='test')
        result = False
        for img in images:
            if tag in img['RepoTags'][0]:
                result = True
        assert result


    @pytest.mark.skipif('"skip"')
    def test_create_container(self):
        print '[TestDockerClient.test_create_container()]'
        tag = 'test/test_build_apache2'
        ports = [22, 80]
        result = self.dockerc.create_container(
            image=tag,
            command=self.command,
            ports=ports
        )
        containers =  self.dockerc.containers(name='test', all=True)
        result = False
        for c in containers:
            if tag in c['Image']:
                result = True
        assert result


    @pytest.mark.skipif('"skip"')
    def test_create_container_error_of_not_image(self):
        print '[TestDockerClient.test_create_container()]'
        tag = 'test/error'
        ports = [22, 80]
        result = self.dockerc.create_container(
            image=tag,
            command=self.command,
            ports=ports
        )
        assert result == None


    @pytest.mark.skipif('"skip"')
    def test_start(self):
        print '[TestDockerClient.test_start()]'
        tag = 'test/test_start_stop_apache2'
        res = self.dockerc.build(
            image=self.image,
            app=self.app,
            port=self.port,
            id_rsa_pub=self.id_rsa_pub,
            tag=tag
        )
        ports = [22, 80]
        container = self.dockerc.create_container(
            image=tag,
            command=self.command,
            ports=ports
        )
        port_bindings={22 : None, 80 : None}
        self.dockerc.start(
            container=container,
            port_bindings=port_bindings
        )
        assert len(self.dockerc.containers(name='test')) > 0


    @pytest.mark.skipif('"skip"')
    def test_start_noset_port_and_sshkey(self):
        print '[TestDockerClient.test_start_noset_port_and_sshkey()]'
        tag = 'test/test_noset_port_and_sshkey'
        res = self.dockerc.build(
            image=self.image,
            app=self.app,
            port=[0],
            id_rsa_pub='',
            tag=tag
        )
        ports = [0]
        container = self.dockerc.create_container(
            image=tag,
            command=self.command,
            ports=ports
        )
        port_bindings={}
        self.dockerc.start(
            container=container,
            port_bindings=port_bindings
        )
        assert len(self.dockerc.containers(name='test')) > 0


    @pytest.mark.skipif('"skip"')
    def test_stop(self):
        print '[TestDockerClient.test_stop()]'
        tag = 'test/test_start_stop_apache2'
        ports = [22, 80]
        container = self.dockerc.create_container(
            image=tag,
            command=self.command,
            ports=ports
        )
        port_bindings={22 : None, 80 : None}
        self.dockerc.start(container=container, port_bindings=port_bindings)
        before = len(self.dockerc.containers(name='test'))
        self.dockerc.stop(container=container)
        after = len(self.dockerc.containers(name='test'))
        assert  before != after


    @pytest.mark.skipif('"skip"')
    def test_remove_container(self):
        print '[TestDockerClient.test_remove_container()]'
        tag = 'test/test_start_stop_apache2'
        ports = [22, 80]
        container = self.dockerc.create_container(
            image=tag,
            command=self.command,
            ports=ports
        )
        port_bindings={22 : None, 80 : None}
        self.dockerc.start(container=container, port_bindings=port_bindings)
        self.dockerc.stop(container=container)
        before = len(self.dockerc.containers(all=True))
        self.dockerc.remove_container(container=container)
        after = len(self.dockerc.containers(all=True))
        assert  before != after


    @pytest.mark.skipif('"skip"')
    def test_remove_image(self):
        print '[TestDockerClient.test_remove_image()]'
        print '[TODO]'
        assert True


    def tearDown(self):
        # kill and remove containers
        containers =  self.dockerc.containers(name='test')
        for c in containers:
            self.dockerc.stop(container=c['Id'])
        containers =  self.dockerc.containers(all=True)
        for c in containers:
            self.dockerc.remove_container(container=c['Id'])
