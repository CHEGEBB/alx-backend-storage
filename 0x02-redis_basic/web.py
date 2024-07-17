#!/usr/bin/env python3
'''A module with tools for caching and tracking web requests.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''The module-level Redis instance for caching and tracking.
'''


def data_cacher(method: Callable) -> Callable:
    '''Decorator to cache the output of data-fetching functions.
    '''
    @wraps(method)
    def invoker(url: str) -> str:
        '''Caches the output of the method and tracks the request count.
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Fetches the content of a URL, caches the response,
      and tracks the request.
    '''
    return requests.get(url).text
