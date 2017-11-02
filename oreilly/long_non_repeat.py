# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/long-non-repeat/
"""


def non_repeat(text: str) -> str:
    """
    The function return the longest string on variable text,
    in which the same characters are not repeated
    'aaaaaa' -> 'a'
    'abdjwawk' -> 'abdjw'
    'abcabcffab' -> 'abcf'
    """
    result_win = ''
    result_text = ''
    for char in text:
        if char in result_text:
            for iterable in range(len(result_text)):
                if char == result_text[iterable]:
                    result_text = result_text[1 + iterable:] + char
                    break
        else:
            result_text += char
        if len(result_win) < len(result_text):
            result_win = result_text
    return result_win
