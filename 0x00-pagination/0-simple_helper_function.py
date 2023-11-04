#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page (int): the current page
        page_size (int): the amount of items in a page
    Returns:
        (tuple): a tuple of size two containing a start index and an end index
    """
    nextPageIndex = page * page_size
    return nextPageIndex - page_size, nextPageIndex
