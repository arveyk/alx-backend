#!/usr/bin/python3
"""FIFOCache
"""
from collections import Counter
BaseCaching = __import__('0-basic_cache').BaseCaching


def CallCount(func):
    """Counter function
    Args:
        args:
        kwargs:
    Returns: list of funtion args"""
    def wrapped(*args):
        wrapped.Tup = args
        return func(*args)
    wrapped.Tup = (0, 0)
    return wrapped


class MRUCache(BaseCaching):
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

            if limit > BaseCaching.MAX_ITEMS:
                LrUsed = self.get.Tup
                List_keys = list(self.cache_data.keys())

                LruDict = {}
                # Get the keys
                for key in List_keys:
                    LruDict[key] = 0
                # increment values
                for key in LruDict:
                    if key == LrUsed[1]:
                        LruDict[key] += 1
                least = LruDict[List_keys[0]]
                least_key = List_keys[0]

                for key in LruDict:
                    if least > LruDict[key]:
                        least_key = key
                        least = LruDict[key]
                if List_keys[0] == least_key:
                    self.cache_data.pop(least_key)
                    p = least_key
                else:
                    self.cache_data.pop(List_keys[0])
                    p = List_keys[0]
                print("DISCARD: {}".format(p))

    @CallCount
    def get(self, key):
        """Getter for cache_data whose value is at given key
        Args:
            key: the key to search
        Returns: the value of the cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
