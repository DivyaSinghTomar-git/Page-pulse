import time


class MemoryCache:

    def __init__(self):
        self.cache = {}

    def get(self, key):

        value = self.cache.get(key)

        if not value:
            return None

        if value["expiry"] < time.time():
            del self.cache[key]
            return None

        return value["data"]

    def set(self, key, data, ttl):

        self.cache[key] = {
            "data": data,
            "expiry": time.time() + ttl
        }