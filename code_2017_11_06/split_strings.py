# -*- coding: utf-8 -*-
"""
Task from
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
"""


def split_strings_to_two_char(*, text: str) -> list:
    """
    Complete the solution so that it splits the string into pairs of two characters.
    If the string contains an odd number of characters then it should replace
    the missing second character of the final pair with an underscore ('_').
    for example:
        split_strings_to_two_char('abc') -> ['ab', 'c_']
        split_strings_to_two_char('abcdef') -> ['ab', 'cd', 'ef']
    """
    if len(text) % 2 == 1:
        text += '_'
    result = []
    for iterable in range(len(text)//2):
        result.append(text[iterable * 2: iterable * 2 + 2])
    return result

split_strings_to_two_char(text='asdfadsf')
