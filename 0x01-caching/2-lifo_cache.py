#!/usr/bin/env python3
"""LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """a caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """documentation"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """docs"""
        return self.cache_data.get(key)
