# -*- coding: utf-8 -*-
"""
Task from
http://www.codewars.com/kata/where-my-anagrams-at/train/python
"""


def anagrams(*, key_word: str, words_to_check: list) -> list:
    """
    function checks if two words are anagrams of each other if they both contain the same letters.
    Args:
        key_word: string
        words_to_check: list of string
    Return:
        List of word with words_to_check where is the same letters as key_word
    For example:
        anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) -> ['aabb', 'bbaa']
    """
    # result = []
    # for word in words_to_check:
    #     if sorted(key_word) == sorted(word):
    #         result.append(word)
    result = [word for word in words_to_check if sorted(key_word) == sorted(word)]
    return result
