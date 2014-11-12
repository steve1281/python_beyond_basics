import socket

class Resolver:
    #called once, when instance is created.
    # ie. Resolver()
    def __init__(self):
        self._cache = {}

    #allows you to call the instance of the class directly
    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
            return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self,host):
        return host in self._cache

