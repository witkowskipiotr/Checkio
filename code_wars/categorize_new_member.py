# -*- coding: utf-8 -*-
"""
Task from
https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
"""

def check_categorize(old: int, handicap: int) -> str:
    """
    Slave function to check categorize membership
    Call in open_or_senior
    """
    return 'Senior' if old >= 55 and handicap > 7 else 'Open'


def open_or_senior(data: list) -> list:
    """
        The Western Suburbs Croquet Club has two categories of membership,
    Senior and Open. They would like your help with an application
    form that will tell prospective members which category they will be placed.
        To be a senior, a member must be at least 55 years old and have
    a handicap greater than 7. In this croquet club, handicaps range from -2 to +26;
    the better the player the lower the handicap.
    Args:
        data: list list of pair int
    return: return list of categorize each element to open or senior
    For example:
        [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]] ->
        -> ["Open", "Open", "Senior", "Open", "Open", "Senior"]
    """
    result = []
    for [old, handicap] in data:
        result.append(check_categorize(old=old, handicap=handicap))
    return result
