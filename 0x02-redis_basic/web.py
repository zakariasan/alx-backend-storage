#!/usr/bin/env python3
""" Redis client module
"""
import requests
from functools import wraps
import redis
from typing import Callable


def cache_page(func: Callable) -> Callable:
    """ cache page """
    @wraps(func)
    def wrapper(url: str) -> str:
        """ wrapper the wrapper """
        cache = redis.Redis()
        cache.incr(f'count:{url}')
        key = f"{url}"
        content = cache.get(key)
        if content:
            return content.decode('utf-8')

        response = func(url)
        cache.set(f'{url}', response, 10)
        return response
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """ get page str """
    response = requests.get(url)
    return response.text
