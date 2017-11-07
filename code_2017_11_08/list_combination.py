# -*- coding: utf-8 -*-
"""
Task
"""


def list_combination(*, first_list: list, second_list: list) -> list:
    """
    Function combines two lists by alternatingly taking elements
    two lists have the same length.
    For example:
        list_combination(first_list=['a', 'b', 'c'], second_list=[1, 2, 3]) -> ['a', 1, 'b', 2, 'c', 3]
    """
    result = []
    for first, second in zip(first_list, second_list):
        result += [first, second]
    return result

list_combination(first_list=['a', 'b', 'c'], second_list=[1, 2, 3])
