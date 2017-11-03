# -*- coding: utf-8 -*-
"""
Task from
https://www.codewars.com/kata/counting-duplicates/train/python
"""


def duplicate_count(text: str) -> int:
    """
    The function return the count of distinct case-insensitive alphabetic characters
    and numeric digits that occur more than once in the input string.
    The input string can be assumed to contain only alphabets
    (both uppercase and lowercase) and numeric digits.
    Example:
    "abcde" -> 0 # no characters repeats more than once
    "aabbcde" -> 2 # 'a' and 'b'
    "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
    "indivisibility" -> 1 # 'i' occurs six times
    "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
    "aA11" -> 2 # 'a' and '1'
    "ABBA" -> 2 # 'A' and 'B' each occur twice
    """

    max_count = 0
    char_exclude = []
    for char in text:
        if char.isalpha():
            text = text.replace(char, char.lower())
            char = char.lower()
        if char not in char_exclude and text.count(char) > 1:
            char_exclude.append(char)
            max_count += 1
    return max_count
