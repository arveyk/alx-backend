#!/usr/bin/python3
"""FIFOCache
"""
from collections import Counter
BaseCaching = __import__('0-basic_cache').BaseCaching


class LRUCache(BaseCaching):
    """First In First Out
    """
    def __init__(self):
        """Initialize the class
        """
        super().__init__()

    def put(self, key, item):
        """Inserts data into cache
        Args:
            key: dictionary key to be used
            items: data to be stored
        Return: no return value
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            limit = len(self.cache_data)
            self.count = Counter()
            if limit > BaseCaching.MAX_ITEMS:
                List_keys = list(self.cache_data.keys())
                print("DISCARD: {}".format(self.count))
                self.cache_data.pop(List_keys[-1])

    def get(self, key):
        """Getter for cache_data whose value is at given key
        Args:
            key: the key to search
        Returns: the value of the cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
