# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/monkey-typing/
"""


def monkey_typing(text: str, words: set) -> int:
    """
    Count how many words are included in the given text. A word should be whole
    and may be a part of other word. Text letter case does not matter.
    Words are given in lowercase and don't repeat. If a word appears several times
    in the text, it should be counted only once.
    :return: The number of words in the text as an integer.
    """
    # simple solution
    # counter = [chunk for chunk in words if chunk in text.lower()]

    # my solution
    text_split = text.lower().split(" ")
    if not all(len(w) >= 3 and w.islower() and w.isalpha for w in words):
        return 0
    score = 0
    eliminated = []
    for text_chunk in text_split:
        words_to_count = words
        for word in words_to_count:
            if word.lower() in text_chunk and word.lower() not in eliminated:
                score += 1
                eliminated.append(word)
    return score
