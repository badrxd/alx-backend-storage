#!/usr/bin/env python3
"""Cache class"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class"""

    def __init__(self):
        """init class cache"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """insert data, and return the key"""

        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
