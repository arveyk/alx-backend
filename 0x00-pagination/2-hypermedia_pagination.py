#!/usr/bin/env python3
"""
Module to create get_hyper function
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Index range function
    Args:
        page: start page
        page_size: number of pages
    Returns: tuple
    """
    if page <= 1:
        size = 0
    else:
        size = page
    pagination = ((page - 1) * page_size, page_size * page)
    return pagination


class Server:
    """Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function description
        """
        assert isinstance(page, int) and type(page_size) is int,\
            f'raised when page and/or page_size are not ints'
        assert page > 0 and page_size > 0, f'raised with negative values'

        search = index_range(page, page_size)
        search_list = []
        data_set = self.dataset()
        if len(data_set) < search[1]:
            return []
        for row in range(search[0], search[1]):
            search_list.append(data_set[row])
        return search_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """FUnction description
        """
        page_listing = self.get_page(page, page_size)
        hyper = {}
        '''if len(page_listing) > 0:
        '''
        totalPages = len(self.__dataset)
        hyper["page_size"] = page_size
        hyper["page"] = page
        if page >= totalPages:
            hyper["data"] = []
            hyper["next_page"] = None
        else:
            end = page + page_size
            hyper["data"] = page_listing
            hyper["next_page"] = page + 1
        if page == 0:
            hyper["previouse_page"] = None
        else:
            hyper["previouse_page"] = page - 1
        no_of_pages = round(totalPages / page_size)
        hyper["total_pages"] = no_of_pages
        if hyper["total_pages"] < (totalPages / page_size):
            hyper["total_pages"] += 1

        return hyper
