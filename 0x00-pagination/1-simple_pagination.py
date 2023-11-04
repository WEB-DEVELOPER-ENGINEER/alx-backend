#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"
    index_range = __import__('0-simple_helper_function').index_range

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
            page (int): page number
            page_size (int): number of items per page
        Returns:
            (List[List]): a list of list(row) if inputs are within range
            ([]) : an empty list if page and page_size are out of range
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]
