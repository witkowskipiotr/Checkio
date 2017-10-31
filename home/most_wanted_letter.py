# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/most-wanted-letter/
"""


def most_wanted_letter(text: str) -> str:
    """
    :param text: a text for analysis as a string
    :return: the most frequent letter in lower case as a string
    """
    text = text.lower()
    value_included = "abcdefghijklmnopqrstuvwxyz"
    value_amount = {}
    for char in text:
        if char in value_included:
            if char not in value_amount.keys():
                value_amount[char] = 1
            else:
                value_amount[char] += 1
    value_most_appearances = max(value_amount.values())
    result = [key for key in value_amount if value_amount[key] == value_most_appearances]

    # if you have two or more letters with the same frequency,
    # then return the letter which comes first in the latin alphabet
    return sorted(result)[0]
