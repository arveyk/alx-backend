#!/usr/bin/python3
"""FIFOCache
"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class MRUCache(BaseCaching):
    """First In First Out
    """
    MruDict = {}
    swt = 0

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

            if self.swt == 0:
                for ky in List_keys:
                    self.MruDict[key] = 0
                self.swt = 1
            else:
                for ky in List_keys:
                    if ky in self.MruDict:
                        continue
                    self.MruDict[ky] = 0

            if limit > BaseCaching.MAX_ITEMS:
                great = self.MruDict[List_keys[0]]
                great_key = List_keys[0]

                tempMruD = self.MruDict
                for key in List_keys:
                    if great <= tempMruD[key]:
                        great_key = key
                        great = tempMruD[key]
                if List_keys[0] == great_key:
                    self.cache_data.pop(List_keys[-2])
                    p = List_keys[-2]
                else:
                    print(self.cache_data[great_key])
                    self.cache_data.pop(great_key)
                    p = great_key
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
                self.MruDict[key] += 1
        if key in self.cache_data:
            return self.cache_data[key]

        return None
