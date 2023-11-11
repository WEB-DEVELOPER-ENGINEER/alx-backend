#!/usr/bin/env python3
"""
LRU Caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache
    """

    def __init__(self):
        """
        Init method
        """
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        """
        assign to the dict 'self.cache_data' the item value for the key 'key'
        """
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            item_discarded = next(iter(self.lru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)
            self.lru_order.popitem(last=False)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
