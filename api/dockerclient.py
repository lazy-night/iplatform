import docker


class DockerClient:

    def __init__(self, name, age):
        # print '[Person.__init__]'
        # self.name = name
        # self.age = age
        c = docker.Client(
            base_url='unix://var/run/docker.sock',
            version='1.12',
            timeout=10
        )

    def showinfo(self):
        print '[Person.showinfo]'
        print '%s (%d)' % (self.name, self.age)
