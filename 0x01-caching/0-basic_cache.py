#!/usr/bin/python3
"""Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    This caching system doesn’t have limit
    """
    def put(self, key, item):
        """
        assign to the dict self.cache_data the item value for the key 'key'
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
