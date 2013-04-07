import redis
from django.core.cache.backends.base import BaseCache


class Redis(BaseCache):

    def __init__(self, host='localhost', port=6379, db=0):
        # self._host = host
        # self._port = port
        # self._db = db
        # self.connect()
        self.r = redis.StrictRedis('localhost', 6379, db=0)

    # def connect(self):
    #     self.r = redis.StrictRedis(self._host, self._port, self._db)
    #     if self.r is not False:
    #         return True
    #     else:
    #         return False

    # def __getattr__(self, name):
    #     pass

    def redis(self):
        return self.r

    def dbsize(self):
        return self.r.execute_command('DBSIZE')

    ##Commands

    def append(self,  *args, **kwargs):
        return self.r.append(*args, **kwargs)

    def set(self,  *args, **kwargs):
        return self.r.set(*args, **kwargs)

    def get(self,  *args, **kwargs):
        return self.r.get(*args, **kwargs)

    def incr(self,  *args, **kwargs):
        return self.r.incr(*args, **kwargs)

    def incrby(self,  *args, **kwargs):
        return self.r.incrby(*args, **kwargs)

    def decrby(self,  *args, **kwargs):
        return self.r.decrby(*args, **kwargs)

    def decr(self,  *args, **kwargs):
        return self.r.decr(*args, **kwargs)

    def setnx(self,  *args, **kwargs):
        return self.r.setnx(*args, **kwargs)

    def delete(self,  *args, **kwargs):
        return self.r.delete(*args, **kwargs)

    def exists(self,  *args, **kwargs):
        return self.r.exists(*args, **kwargs)

    def rename(self,  *args, **kwargs):
        return self.r.rename(*args, **kwargs)
