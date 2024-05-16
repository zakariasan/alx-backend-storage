#!/usr/bin/env python3
""" Redis client module
"""
import requests
from functools import wraps
import redis


def cache_page(func):
    """ cache page """
    @wraps(func)
    def wrapper(url: str) -> str:
        """ wrapper the wrapper """
        cache = redis.Redis()
        key = f"count:{url}"
        content = cache.get(key)
        if content:
            return content.decode()

        response = func(url)
        cache.setex(key, 10, response)
        return response
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """ get page str """
    response = requests.get(url)
    return response.text


