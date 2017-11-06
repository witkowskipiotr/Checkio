# -*- coding: utf-8 -*-
"""
Task from
http://www.codewars.com/kata/does-my-number-look-big-in-this/train/python
"""


def narcissistic(*, value: int) -> bool:
    """
    A Narcissistic Number is a number which is the sum of its own digits,
    each raised to the power of the number of digits.
    Args:
        value:
    Return: true or false depending upon whether
            the given number is a Narcissistic number
    For example:
        take 153 (3 digits): 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    """
    # solution one line code
    # return sum([int(number)**len(str(value)) for number in str(value)]) == value
    if not value:
        return False

    result = 0
    for number in str(value):
        result += int(number)**len(str(value))
    return result == value
