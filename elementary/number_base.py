# -*- coding: utf-8 -*-
"""
Simple functions from
https://py.checkio.org/mission/number-radix/
"""


def number_base(str_number: str, radix: int) -> int:
    """
    Convert number of radix system to decimal system
    :param str_number: value of number string in some numerical system
    :param radix: tells us about the system
    in which the numerical value is stored - between 2 and 36
    :return: integer in decimal system or -1 if can`t convert number
    """
    valid_number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valid_number_assignment = {num: i for i, num in enumerate(valid_number)}
    result = 0
    # reverse enumerate str_number to sum result
    for i, number in enumerate(str_number[::-1]):
        if number in valid_number[:radix]:
            chunk = int(valid_number_assignment[number]) * radix ** i
            result += chunk
        else:
            return -1
    return result
