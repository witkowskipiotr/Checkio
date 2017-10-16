# -*- coding: utf-8 -*-
"""
Simple functions from
https://py.checkio.org/mission/absolute-sorting/
"""


def absolute_sorting(numbers_to_sort: tuple) -> list:
    """we sort, no meaning positive and negative numbers
    :param numbers_to_sort: An array of numbers, a tuple
    :return: the list sorted by absolute values in ascending order
    """
    numbers_sorted = sorted(set(abs(x) for x in numbers_to_sort))
    if len(numbers_sorted) != len(numbers_to_sort):
        return ["Any numbers is duplicate"]
    result = []
    for num_sorted in numbers_sorted:
        for num_to_sort in numbers_to_sort:
            if num_sorted == abs(num_to_sort):
                result.append(num_to_sort)
    return result
