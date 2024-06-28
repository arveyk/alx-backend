#!/usr/bin/python3
"""FIFOCache
"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class LRUCache(BaseCaching):
    """First In First Out
    """
    LruDict = {}
    swt = 0
    count = 0

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
            List_keys = list(self.cache_data.keys())

            #if self.swt == 0:
            #    for ky in List_keys:
            #        self.LruDict[ky] = 0
            #    self.swt = 1
            #else:
            for ky in List_keys:
                if ky in self.LruDict:
                    continue
                self.LruDict[ky] = 0
                self.count += 1

            if limit > BaseCaching.MAX_ITEMS:
                least = self.LruDict[List_keys[0]]
                least_key = List_keys[0]
                great = least
                gKey = least_key

                tempLruD = self.LruDict
                for ky in List_keys:
                    if least > tempLruD[ky]:
                        least_key = ky
                        least = tempLruD[ky]
                    if great < tempLruD[ky]:
                        gKey = ky
                        great = tempLruD[ky]
                #if List_keys[0] == least_key:
                if self.count >= 3 and gKey == self.cache_data[List_keys[0]]:
                    self.cache_data.pop(List_keys[0])
                    self.LruDict.pop(List_keys[0])
                    p = List_keys[0]
                    self.count = 0
                else:
                    self.cache_data.pop(least_key)
                    self.LruDict.pop(least_key)
                    p = least_key
                print("DISCARD: {}".format(p))

    def get(self, key):
        """Getter for cache_data whose value is at given key
        Args:
            key: the key to search
        Returns: the value of the cache_data
        """
        List_keys = list(self.cache_data.keys())
        for ky in List_keys:
            if key == ky:
                self.LruDict[ky] += 1
        if key in self.cache_data:
            return self.cache_data[key]

        return None
