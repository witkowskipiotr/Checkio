# -*- coding: utf-8 -*-
"""
functions from empireofcode.com/game/#
"""


def count_units(number):
    """
    :param number: A number as a positive integer
    :return: The quantity of units in binary form as an integer
    """
    amount_units_positive = str(bin(number)).replace("0", "").replace("b", "")
    return len(amount_units_positive)
