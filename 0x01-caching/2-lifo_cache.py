#!/usr/bin/env python3
"""LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """a caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """assign to the dict self.cache_data the value for the key 'key'"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)
            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key)
