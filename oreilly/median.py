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
    Args:
        numbers: An array as a list of integers.
    return:
        The median as a float or an integer.
    for example:
    median_set_of_numbers([3, 1, 2, 5, 3]) -> 3
    median_set_of_numbers([1, 300, 2, 200, 1]) -> 2
    median_set_of_numbers([3, 6, 20, 99, 10, 15]) -> 12.5
    """
    numbers = sorted(numbers)
    count = len(numbers)
    if count % 2 == 0:
        return (numbers[(count // 2) - 1] + numbers[count // 2]) / 2
    return numbers[int(count / 2)]
