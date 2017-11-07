# -*- coding: utf-8 -*-
"""
Task from
https://www.codewars.com/kata/convert-string-to-camel-case/train/python
"""


def changelings_camel_case(*, text: str, sign: str) -> str:
    """
    slave function call on to_camel_case
    Args:
        text: interesting text to replace camel case
        sign: the sign followed by the change camel case
    Return:
        changed text where sign signs occurred
    for example:
        changelings_camel_case(text='a-b_c', sign='-') -> 'aB_c'
    """
    result = ''
    text_split = text.split(sign)
    for iterable, word in enumerate(text_split):
        if iterable == 0 and text[:len(word)] == word:
            result += word
        else:
            result += word[0].upper() + word[1:]
    return result


def to_camel_case(*, text: str) -> str:
    """
    Main function
    Converts dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized only
    if the original word was capitalized.
    return:
        replace capital letters to hight where before is sign '-' and '_'
        this sign is removed
    for example:
        changelings_camel_case(text='a-b_c', sign='-') -> 'aBC'
    """
    result = changelings_camel_case(text=text, sign='-')
    return changelings_camel_case(text=result, sign='_')
