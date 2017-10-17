# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/min-max/
"""


def min(*args, **kwargs):
    """
    alternative func to min
    :param args: One positional argument as an iterable
    or two or more positional arguments
    :param kwargs: Optional keyword argument as a function
    :return:The smallest for the "min" function.
    """
    key = kwargs.get("key", lambda x: x)
    args = args[0] if len(args) == 1 else args[:]
    min_value = ""
    for arg in args:
        if min_value == "":
            min_value = arg
        min_value = arg if key(arg) < key(min_value) else min_value
    return min_value


def max(*args, **kwargs):
    """
    alternative func to max
    :param args: One positional argument as an iterable
    or two or more positional arguments
    :param kwargs: Optional keyword argument as a function
    :return:The largest for the "max" function.
    """
    key = kwargs.get("key", lambda x: x)
    args = args[0] if len(args) == 1 else args[:]
    max_value = ""
    for arg in args:
        if max_value == "":
            max_value = arg
        max_value = arg if key(arg) > key(max_value) else max_value
    return max_value
