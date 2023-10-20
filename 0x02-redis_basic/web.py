#!/usr/bin/env python3
"""A module for caching data and tracking the number of accesses."""
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()


def data_cacher(func: Callable[[str], str]) -> Callable[[str], str]:
    """A decorator that caches data and tracks the number of accesses."""

    @wraps(func)
    def wrapper(url: str) -> str:
        """The wrapper function for caching the output."""
        redis_store.incr(f"count:{url}")

        result = redis_store.get(f"result:{url}")
        if result is not None:
            return result.decode("utf-8")

        result = func(url)
        redis_store.setex(f"result:{url}", 10, result)
        return result

    return wrapper


@data_cacher
def get_page(url: str) -> str:
    """Fetch the content of a URL."""
    return requests.get(url).text
