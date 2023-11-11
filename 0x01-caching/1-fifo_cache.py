#!/usr/bin/python3
"""FIFO caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching
    """
    def __init__(self):
        """Instantiation method
        """
        super().__init__()
        self.i = 0

    def put(self, key, item):
        """
        assign to the dict self.cache_data the item value for the key 'key'
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
