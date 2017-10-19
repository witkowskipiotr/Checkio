# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/long-non-repeat/
"""

#TODO not finished

def non_repeat(text: str) -> str:
    result_win = ''
    result_text = ''
    result_count = 0
    for char in text:
        if char in result_text:
            result_text = char
        else:
            result_text += char
        if len(result_text) > result_count:
            result_win = result_text
    return result_count

print(non_repeat('aaaaa') == 'a')
print(non_repeat('abdjwawk') == 'abdjw')
print(non_repeat('abcabcffab') == 'abcf')