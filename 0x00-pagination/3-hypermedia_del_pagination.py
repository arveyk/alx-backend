#!/usr/bin/env python3
"""
Module for
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    Attributes:
        __dataset (list): row data
        __indexed_dataset (list): indexed, searched data
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Init method to initialize instances
        Args: no arguments
        Return: no return values
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        Args:
            None
        Returns: list of lists
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        Args:
            none
        Returns: an indexed data set
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """ Function to get index media even if some is deleted
        Args:
            index: current start index
            page_size: size of data to index
        Returns: indexed data set
        """
        assert isinstance(index, int)
        assert isinstance(page_size, int) and page_size > 0
        assert index >= 0 and index < 3000, f"raised when out of range"
        hyper_index = {}
        hyper_index["index"] = index
        hyper_index["page_size"] = page_size
        hyper_index["next_index"] = index + page_size
        hyper_index["page_size"] = page_size
        end = page_size + index
        hyper_index["data"] = self.__dataset[index: end]
        return hyper_index
