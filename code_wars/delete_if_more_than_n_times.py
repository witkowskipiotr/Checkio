# -*- coding: utf-8 -*-
"""
Task from
https://www.codewars.com/kata/delete-occurrences-of-an
-element-if-it-occurs-more-than-n-times/train/python
"""


def delete_if_occurs_more_than_n(order: list, max_element: int) -> list:
    """
    Given a list lst and a number N, create a new list that contains each number
    of lst at most N times without reordering.
    For example:
        order = [1,2,3,1,2,1,2,3], max_element = 2 -> [1,2,3,1,2],
    drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times,
    and then take 3, which leads to [1,2,3,1,2,3].
    """
    order.reverse()
    while True:
        iterable = 0
        for item in order:
            if order.count(item) > max_element:
                order.remove(item)
                break
            iterable += 1
        if iterable == len(order):
            break
    order.reverse()
    return order
