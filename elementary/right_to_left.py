# -*- coding: utf-8 -*-
"""Simple functions from https://py.checkio.org/mission/right-to-left/"""

def right_to_left(phrases: tuple) -> str:
    """Join strings and replace "right" to "left"
    You are given a sequence of strings. You should join these strings into chunk of text
    where the initial strings are separated by commas. As a joke on the right handed robots,
    you should replace all cases of the words "right" with the word "left",
    even if it's a part of another word. All strings are given in lowercase.
    :param sequence of strings as a tuple of strings
    :return: text as a string
    """
    if not phrases or len(phrases) > 42:
        return ""
    return ",".join(phrases).replace("right", "left")
