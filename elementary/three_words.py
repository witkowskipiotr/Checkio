# -*- coding: utf-8 -*-
"""Simple functions from https://py.checkio.org/"""

def three_words(text: str) -> bool:
    """
    """
    if len(text) == 0:
        return False
    if len(text) > 100:
        return False
    number = "0123456789"
    divided_text = text.split(" ")
    for part in divided_text:
        word = True

        for character in part:
            if character in number:
                word = False


three_words("czsd 3 sdfas sdfas 3 sfs sdf sdf 4")
