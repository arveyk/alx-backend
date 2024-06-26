#!/usr/bin/python3
"""BasicCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Inserts data into the cache
        Args:
            key: the key to use in the dictionary data cache
            items: the value to store
        Returns: no return value
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Getter for cache_data whose value is at given key
        Args:
            key: the key to search
        Returns: the value of the cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
