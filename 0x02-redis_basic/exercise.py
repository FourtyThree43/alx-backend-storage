#!/usr/bin/env python3
"""
Module for the Cache class
"""
import redis
import uuid
from typing import Union, Callable, Optional

from redis.commands.core import ResponseT


class Cache:
    """
    Class for cache
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable]) -> ResponseT:
        """
        Get the data
        """
        data = self._redis.get(key)

        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> ResponseT:
        """
        Get the data as string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> ResponseT:
        """
        Get the data as int
        """
        return self.get(key, int)
