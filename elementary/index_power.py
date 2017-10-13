# -*- coding: utf-8 -*-
"""Simple functions from https://py.checkio.org/"""

def index_power(table: list, num: int) -> int:
    """
    Find Nth power of the element with index N.
    Given an array with positive numbers and a num.
    If num is outside of the table, then return -1.
    else value of index num table to power num
    :param table: list integers
    :param index: number of list
    """
    if not table:
        return -1
    if len(table) > 10:
        return -1

    return table[num] ** num if len(table) > num else -1
