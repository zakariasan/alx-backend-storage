#!/usr/bin/env python3
""" Redis client module
"""
import redis
import uuid
from typing import Union, Any, Callable, Optional
from functools import wraps


def replay(method: Callable) -> None:
    """Display the history of calls for a particular function."""

    client = redis.Redis()
    key = method.__qualname__
    calls = client.get(method.__qualname__).decode('utf-8')
    inputs = [input.decode('utf-8') for input in
              client.lrange(f'{method.__qualname__}:inputs', 0, -1)]
    outputs = [output.decode('utf-8') for output in
               client.lrange(f'{method.__qualname__}:outputs', 0, -1)]
    print(f"{key} was called {calls} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{key}(*{inp.decode()}) -> {out.decode()}")


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""
    @wraps(method)
    def wrap(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", output)
        return output
    return wrap


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""
    @wraps(method)
    def wrap(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrap


class Cache:
    """ class caching"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str, fn: Optional[Callable] = None) -> Any:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)
