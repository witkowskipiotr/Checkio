# -*- coding: utf-8 -*-
"""Simple functions from https://py.checkio.org/"""

def three_words(text: str) -> bool:
    """
    In the string we check if there are three words one by one
    :param text: string to check
    :return: positive when three words is one by one,
            negative otherwise
    """
    if not text:
        return False
    if len(text) > 100:
        return False
    nums = "0123456789"
    number_word_one_by_one = 0
    divided_text = text.split(" ")
    for part in divided_text:
        is_word = True
        for character in part:
            if character in nums:
                is_word = False
                number_word_one_by_one = 0
        if is_word:
            number_word_one_by_one += 1
            if number_word_one_by_one == 3:
                return True
    return False
