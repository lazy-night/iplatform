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
            image='ubuntu:14.04', app='', port='80',
            command='"/usr/sbin/apache2", "-D", "FOREGROUND"',
            tag='koide/test_apache2')
        assert len(self.dockerc.images(name='koide')) > 2


    def test_create_container(self):
        print '[TestDockerClient.test_create_container()]'
        image = 'koide/test_apache2'
        ports = [80]
        result = self.dockerc.create_container(image=image, ports=ports)
        assert len(self.dockerc.containers(name='koide', all=True)) > 0


    def test_start(self):
        print '[TestDockerClient.test_start()]'
        tag = 'koide/test_apache2'
        res = self.dockerc.build(image='ubuntu:14.04', app='', port='80',
            command='"/usr/sbin/apache2ctl", "-D", "FOREGROUND"',
            tag=tag)
        ports = [80]
        container = self.dockerc.create_container(image=tag, ports=ports)
        port_bindings={80 : None}
        self.dockerc.start(container=container, port_bindings=port_bindings)
        assert len(self.dockerc.containers(name='koide')) > 0


    def tearDown(self):
        print '[TODO]'
        # kill and remove containers


# 
# #     def pull(self, repository, tag=None, stream=False):
# #         print '[DockerClient.pull]'
# #         print '[TODO]'
# #         return 'test'
# 
# #     def remove_container(self, container, v=False, link=False):
# #         print '[DockerClient.remove_container]'
# #         print '[TODO]'
# #         return 'test'
# 
# #     def remove_image(self, image):
# #         print '[DockerClient.remove_image]'
# #         print '[TODO]'
# #         return 'test'
# 
# #     def stop(self, container, timeout=10):
# #         print '[DockerClient.stop]'
# #         print '[TODO]'
# #         return 'test'
