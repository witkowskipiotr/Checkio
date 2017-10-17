# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/long-repeat/
"""


def long_repeat(text: str) -> int:
    """
    length the longest substring that consists of the same char
    Find the length of the longest substring that consists of the same letter.
    For example, line "aaabbcaaaa" contains four substrings with the same letters
    "aaa", "bb","c" and "aaaa". The last substring is the longest one
    which makes it an answer.
    """
    if not text:
        return 0
    char_old = ""
    count = 0
    result = []
    for char in text:
        if char == char_old:
            count += 1
        else:
            result.append(count)
            char_old = char
            count = 1
    result.append(count)
    return max(result)
