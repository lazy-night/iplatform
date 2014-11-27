import commands
import docker
import logging
import logging.config
import os
from string import Template


class DockerClient:

    def __init__(self):
        logging.config.fileConfig('./api/logger_config.ini')
        self.logger = logging.getLogger(__name__)
        self.logger.info('[DockerClient.__init__]')
        try:
            self.dockerc = docker.Client(
                ## default
                # base_url='unix://var/run/docker.sock',
                ## degital ocean
                # base_url='tcp://128.199.213.43:4243',
                ## development
                # base_url='tcp://192.168.59.103:2376',
                base_url='tcp://0.0.0.0:4243',
                version='1.12',
                timeout=10
            )
        except Exception as e:
            self.logger.error('=== output error ===')
            self.logger.error('type:' + str(type(e)))
            self.logger.error('args:' + str(e.args))
            self.logger.error('message:' + str(e.message))
            self.logger.error('Exception as e:' + str(e))


    def build(self, image, app, port, id_rsa_pub, tag):
        self.logger.info('[DockerClient.build]')
        workpath = './api/workspace'
        templatepath = image.replace(':', '').replace('.', '')
        templatepath = './api/Dockerfile/template/Dockerfile.template' + templatepath
        values = {}
        values['image'] = app
        values['user'] = tag.split('/')[0]
        port_str = ''
        for p in port:
            port_str = port_str + ' ' + str(p)
        values['port'] = port_str
        values['id_rsa_pub'] = id_rsa_pub

        with open(templatepath, 'rt') as templatef:
            template = Template(templatef.read())
            converted = template.substitute(values)
            with open(os.path.join(workpath, 'Dockerfile'), 'wt') as dockerfilef:
                dockerfilef.write(converted)

        # copy conf directory
        # shutil.copytree('conf',os.path.join(workpath, 'conf'))

        result = self.dockerc.build(path=workpath, tag=tag, rm=True)
        result = list(result)[-1]
        self.logger.info(result)

        imageid = None
        if 'Successfully built' in result:
            imageid = result.replace('{"stream":"Successfully built', '').replace('\\n"}', '')
        else:
            self.logger.error('Failed to build')
        return {'Id': imageid, 'Repository': tag}


    def containers(self, name=None, quiet=False, all=False):
        self.logger.info('[DockerClient.containers]')
        containers = self.dockerc.containers(all=all)
        if all:
            return containers
        res = []
        if name:
            for c in [cs for cs in containers if name in cs['Image']]:
                dic = c
                ports = []
                for p in c['Ports']:
                    ports.append(str(p['PublicPort']) + ' => ' + str(p['PrivatePort']))
                dic['Ports'] = ports
                res.append(dic)
        return res


    def create_container(self, image, ports=None):
        self.logger.info('[DockerClient.create_containers]')
        try:
            container = self.dockerc.create_container(image=image, ports=ports)
            self.logger.info(container)
            return container['Id']
        except Exception as e:
            self.logger.error('=== output error ===')
            self.logger.error('type:' + str(type(e)))
            self.logger.error('args:' + str(e.args))
            self.logger.error('message:' + str(e.message))
            self.logger.error('Exception as e:' + str(e))
        return None


    def images(self, name=None, quiet=False, all=False):
        self.logger.info('[DockerClient.images]')
        images = self.dockerc.images()
        res = []
        if name:
            for img in [imgs for imgs in images if name in imgs['RepoTags'][0].split('/')[0]]:
                dic = {}
                dic['RepoTags'] = img['RepoTags']
                dic['Id'] = img['Id']
                res.append(dic)
        return res


    def remove_container(self, container):
        self.logger.info('[DockerClient.remove_container()]')
        try:
            self.dockerc.remove_container(container=container)
            return True
        except Exception as e:
            self.logger.error('=== output error ===')
            self.logger.error('type:' + str(type(e)))
            self.logger.error('args:' + str(e.args))
            self.logger.error('message:' + str(e.message))
            self.logger.error('Exception as e:' + str(e))
        return False


    def remove_image(self, image):
        self.logger.info('[DockerClient.remove_image()]')
        try:
            self.dockerc.remove_image(image=image)
            return True
        except Exception as e:
            self.logger.error('=== output error ===')
            self.logger.error('type:' + str(type(e)))
            self.logger.error('args:' + str(e.args))
            self.logger.error('message:' + str(e.message))
            self.logger.error('Exception as e:' + str(e))
        return False


    def start(self, container, port_bindings=None):
        self.logger.info('[DockerClient.start()]')
        try:
            self.dockerc.start(container=container, port_bindings=port_bindings)
            return True
        except Exception as e:
            self.logger.error('=== output error ===')
            self.logger.error('type:' + str(type(e)))
            self.logger.error('args:' + str(e.args))
            self.logger.error('message:' + str(e.message))
            self.logger.error('Exception as e:' + str(e))
        return False


    def stop(self, container):
        self.logger.info('[DockerClient.stop()]')
        try:
            self.dockerc.stop(container=container)
            return True
        except Exception as e:
            self.logger.error('=== output error ===')
            self.logger.error('type:' + str(type(e)))
            self.logger.error('args:' + str(e.args))
            self.logger.error('message:' + str(e.message))
            self.logger.error('Exception as e:' + str(e))
        return False

if __name__ == '__main__':
    dockerc = DockerClient()
