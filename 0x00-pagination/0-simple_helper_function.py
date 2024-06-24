#!/usr/bin/env python3
"""Simple pagiation
"""


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
