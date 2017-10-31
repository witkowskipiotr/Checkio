# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/median/
"""


def median_set_of_numbers(numbers: list) -> float:
    """
    A median is a numerical value separating the upper half of a sorted array
    of numbers from the lower half. In a list where there are an odd number of entities,
    the median is the number found in the middle of the array. If the array contains
    an even number of entities, then there is no single middle value,
    instead the median becomes the average of the two numbers found in the middle.
    :param numbers: An array as a list of integers.
    :return: The median as a float or an integer.
    """
    numbers = sorted(numbers)
    count = len(numbers)
    if count % 2 == 0:
        return (numbers[(count // 2) - 1] + numbers[count // 2]) / 2
    return numbers[int(count / 2)]
