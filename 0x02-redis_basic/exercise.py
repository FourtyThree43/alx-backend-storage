#!/usr/bin/env python3
"""
Module for the Cache class
"""
import redis
import uuid
from typing import Union


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