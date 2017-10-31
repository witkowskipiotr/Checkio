# -*- coding: utf-8 -*-
"""
O'Reilly functions from
https://py.checkio.org/mission/create-intervals/
"""


def get_sets_of_unbroken_numbers(var: set) -> list:
    """
    Create a list of intervals out of set of ints.
    """
    if not var:
        return []
    district = []
    is_break = True
    for i in range(min(var), max(var) + 1):
        is_in_collection = True if i in var else False
        if is_break and is_in_collection:
            district.append((min(var), min(var)))
            var.remove(min(var))
        if not is_break and is_in_collection:
            district[-1] = list(district[-1])
            district[-1][1] = min(var)
            district[-1] = tuple(district[-1])
            var.remove(min(var))
        is_break = False if is_in_collection else True
    return district
