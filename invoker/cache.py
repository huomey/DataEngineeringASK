import time
from cachetools import TTLCache
import redis

local_cache = TTLCache(maxsize=3, ttl=10)

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

def get_cache(viewerid):
    if viewerid in local_cache:
        return local_cache[viewerid]
    cache_value = redis_client.get(viewerid)
    if cache_value:
        return cache_value.decode('utf-8')
    return None

def set_cache(viewerid, data):
    local_cache[viewerid] = data
    redis_client.setex(viewerid, 600, data)
