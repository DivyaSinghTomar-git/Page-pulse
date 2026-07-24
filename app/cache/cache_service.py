from app.cache.memory_cache import MemoryCache

cache = MemoryCache()


def get_cached(url):
    return cache.get(url)


def set_cache(url, response, ttl):
    cache.set(url, response, ttl)