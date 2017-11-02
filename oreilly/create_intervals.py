# -*- coding: utf-8 -*-
"""
O'Reilly functions from https://py.checkio.org/mission/create-intervals/
"""


def get_sets_of_unbroken_numbers(var: set) -> list:
    """
    Create a list of intervals out of set of ints.
    Values can only be in the same interval if the difference between a value
    and the next smaller value in the set equals one, otherwise a new interval begins.
    The start value of an interval is excluded from this rule.
    Args
        var: A set of ints.
    return:
        A list of tuples of two ints, indicating the endpoints of the interval.
        The Array should be sorted by start point of each interval
    for example:
        get_sets_of_unbroken_numbers({1, 2, 3, 4, 5, 7, 8, 12}) -> [(1, 5), (7, 8), (12, 12)]
        get_sets_of_unbroken_numbers({1, 2, 3, 6, 7, 8, 4, 5}) -> [(1, 8)]
    """
    if not var:
        return []
    result = []
    is_break = True
    for iterate in range(min(var), max(var) + 1):
        is_in_collection = True if iterate in var else False
        if is_break and is_in_collection:
            result.append((min(var), min(var)))
            var.remove(min(var))
        if not is_break and is_in_collection:
            result[-1] = list(result[-1])
            result[-1][1] = min(var)
            result[-1] = tuple(result[-1])
            var.remove(min(var))
        is_break = False if is_in_collection else True
    return result
