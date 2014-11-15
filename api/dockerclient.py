import commands
import docker
import logging
import logging.config


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
            self.logger.error('message:' + e.message)
            self.logger.error('Exception as e:' + str(e))


    def build(self, path=None, tag=None, quiet=False, fileobj=None,
        nocache=False, rm=False, stream=False,
        timeout=None, custom_context=False, encoding=None):
        self.logger.info('[DockerClient.build]')
        # return self.dockerc.build(path=path, tag=tag)
        workpath = '/var/data'
        values = {}
        values['name'] = 'name'
        values['host'] = 'host'

        with open('Dockerfile.template', 'rt') as templatef:
            template = Template(templatef.read())
            converted = template.substitute(values)
            with open(os.path.join(workpath, 'Dockerfile'), 'wt') as dockerfilef:
                dockerfilef.write(converted)

        # copy conf directory
        shutil.copytree('conf',os.path.join(workpath, 'conf'))

        imagename = 'imagename'
        imageid, result = dockerc.build(path=workpath, tag=imagename, rm=True)
        if not imageid: logging.error('Failed to build: ' + str(result))
        return {'Id': imageid, 'Repository': imagename}


#     def commit(self, container, repository=None, tag=None, message=None, author=None, conf=None):
#         print '[DockerClient.commit]'
#         print '[TODO]'


    def containers(self, name=None, quiet=False, all=False, trunc=True,
        latest=False, since=None, before=None, limit=-1):
        self.logger.info('[DockerClient.containers]')
        containers = self.dockerc.containers()
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


    def create_container(self, image, command=None, hostname=None, user=None,
        detach=False, stdin_open=False, tty=False, mem_limit=0,
        ports=None, environment=None, dns=None, volumes=None,
        volumes_from=None, network_disabled=False, name=None,
        entrypoint=None, cpu_shares=None, working_dir=None,
        memswap_limit=0):
        print '[DockerClient.create_containers]'
        return self.dockerc.createcontainer(image=image, ports=ports)


    def images(self, name=None, quiet=False, all=False, viz=False):
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


    def pull(self, repository, tag=None, stream=False):
        self.logger.info('[DockerClient.pull]')
        return self.dockerc.pull(repository=repository, tag=tag)


    def remove_container(self, container, v=False, link=False):
        print '[DockerClient.remove_container]'
        return self.dockerc.remove_container(container=container)


    def remove_image(self, image):
        print '[DockerClient.remove_image]'
        return self.dockerc.remove_image(image=image)


    def start(self, container, binds=None, port_bindings=None, lxc_conf=None,
        publish_all_ports=False, links=None, privileged=False,
        dns=None, dns_search=None, volumes_from=None, network_mode=None, restart_policy=None):
        print '[DockerClient.start]'
        return self.dockerc.start(container=container, port_bindings=port_bindings)


    def stop(self, container, timeout=10):
        print '[DockerClient.stop]'
        return self.dockerc.stop(container=container)


if __name__ == '__main__':
    # logging.config.fileConfig('logger_config.ini')
    # logger = logging.getLogger(__name__)
    dockerc = DockerClient()

    # print dockerc.images(name='koide')
    # self.logger.info(commands.getoutput('pwd'))

