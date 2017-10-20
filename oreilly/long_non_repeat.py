# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/long-non-repeat/
"""


def non_repeat(text: str) -> str:
    """
        the longest substring without repeating chars
    """
    result_win = ''
    result_text = ''
    for char in text:
        if char in result_text:
            for i in range(len(result_text)):
                if char == result_text[i]:
                    result_text = result_text[1 + i:] + char
                    break
        else:
            result_text += char
        if len(result_win) < len(result_text):
            result_win = result_text
    return result_win
