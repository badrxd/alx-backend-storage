#!/usr/bin/env python3

"""
Implementing an expiring web cache and tracker.
"""

import requests
import redis
from functools import wraps

store_cache = redis.Redis()


def track_url_access(method):
    """counter"""

    @wraps(method)
    def decorated_function(url):
        cached_key = f"cached:{url}"
        cached_data = store_cache.get(cached_key)

        if cached_data:
            return cached_data.decode("utf-8")

        key_counter = f"count:{url}"
        html = method(url)

        store_cache.incr(key_counter)
        store_cache.set(cached_key, html)
        store_cache.expire(cached_key, 10)

        return html

    return decorated_function


@track_url_access
def get_page(url: str) -> str:
    """Returns content"""
    response = requests.get(url)
    return response.text
