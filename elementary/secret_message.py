# -*- coding: utf-8 -*-
"""Simple functions from https://py.checkio.org/"""
import string


def find_message(text: str) -> str:


    """
    Find a secret message
    decode message from text loos after uppercase chars

    :Returns
    uppercase chars from string or None


    """
    if not all(ch in string.printable for ch in text):
        return
    elif not text:
        return ""
    if len(text) > 1000:
        return
    decode_message = ""
    # check case sensitive for a simple character in string
    for correct_char in [char for char in text\
                         if char.upper() == char and char.lower()\
                in 'abcdefghijklmnopqrstuwxyz']:
        decode_message += correct_char
    return decode_message
