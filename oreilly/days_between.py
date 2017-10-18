# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/days-diff/
"""

from datetime import date

def number_days_between_date(date1: tuple, date2: tuple) -> int:
    """
    Find absolute diff in days between dates
    :param date1, date2: Two dates as tuples of integers
    :return: The difference between the dates in days as an integer.
    """
    date1 = date(year=date1[0], month=date1[1], day=date1[2])
    date2 = date(year=date2[0], month=date2[1], day=date2[2])
    return abs((date1-date2).days)
