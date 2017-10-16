# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/non-unique-elements/
"""


def non_unique_elements(data: list) -> list:
    """
    :param array_int: non-empty list of integers
    :return: list non unique numbers
    """
    return [number for number in data if data.count(number) > 1]
