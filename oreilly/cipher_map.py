# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/cipher-map2/
"""


def decode_part_text(cipher_grille: tuple, ciphered_password: tuple) -> str:
    """
    get two tuples. If first have "X" we get her position x & y, read
    second with this position and compose add to result
    """
    result = ""
    for gril, pas in zip(cipher_grille, ciphered_password):
        decode_line = [pas[char] for char in range(len(gril)) if gril[char] == "X"]
        result += "".join(decode_line)
    return result

def rotate_tuple_90(data: tuple) -> tuple:
    """
    rotate 90 degrees clockwise tuple of strings n-elements square (tuple_n x string_n)
    """
    result = ["" for part in range(len(data))]
    for part in range(len(data)):
        for i, element in enumerate(data[part]):
            result[i] = element + result[i]
    return tuple(result)

def recall_ciphered_password(cipher_grille: tuple, ciphered_password: tuple) -> str:
    """
    return decode text
    """
    text = ""
    for num in range(4):
        text += decode_part_text(cipher_grille, ciphered_password)
        cipher_grille = rotate_tuple_90(cipher_grille)
    return text
