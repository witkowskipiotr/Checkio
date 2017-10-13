# -*- coding: utf-8 -*-
"""
Simple functions from
https://py.checkio.org/mission/digits-multiplication/
"""

def digits_multiplication(number: int) -> int:
    """
    Function should calculate the product of the digits
    excluding any zeroes
    :param number: positive integer
    :return: multiple of all chunks number, excluded zeroes
    """
    if not number or number > 10 ** 6:
        return 0
    divided_number_to_string = ([num for num in str(number) if num != "0"])
    result = 1
    for chunk in divided_number_to_string:
        result *= int(chunk)
    return result
