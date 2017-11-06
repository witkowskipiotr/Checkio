# -*- coding: utf-8 -*-
"""
O'Reilly  functions from https://py.checkio.org/mission/cipher-map2/
decrypt data using a simple cipher for two tuple
"""


def decode_part_text(encrypted_data: tuple, ciphered_password: tuple) -> str:
    """
    slave function call in recall_ciphered_password.
    Get two 4x4tuples. We move on loop line and column. If first tuple have char "X"
    in element of tuple, we get value of second tuple (ciphered_password) with the same position
    and add to result.
    for example:
        encrypted_data, ciphered_password -> result
        ('X...',        ('itdf',          -> 'i'
         '..X.',         'gdce',          -> 'c'
         'X..X',         'aton',          -> 'an'
         '....'),        'qrdi')          -> ''
         return: 'ican'
    """
    result = ""
    for data, password in zip(encrypted_data, ciphered_password):
        decode_line = [password[char] for char in range(len(data)) if data[char] == "X"]
        result += "".join(decode_line)
    return result


def rotate_tuple_90_degrees(data: tuple) -> tuple:
    """
    rotate 90 degrees clockwise tuple of strings n-elements square (tuple_n x string_n)
    for example:
        ('itdf', -> ('qagi',
         'gdce',     'rtdt',
         'aton',     'docd',
         'qrdi')     'inef')
    """
    # part is only auxiliary variable
    result = ["" for part in range(len(data))]
    for part in range(len(data)):
        for item, element in enumerate(data[part]):
            result[item] = element + result[item]
    return tuple(result)


def recall_ciphered_password(encrypted_data: tuple, ciphered_password: tuple) -> str:
    """
    Main method in module
    We receive an encrypted message as a 4x4 tuple
    and decryption key in the same size 4x4 tuple.
    I. we Make 4 turns:
        1. decode part text
        2. rotate
    II. reutrn
    Rotate encrypted_data by 90 degrees and read again. After completing 3 turns,
    return message with connection 4-element decode string
    for example:
        encrypted_data, ciphered_password -> result
        ('X...',        ('itdf',
         '..X.',         'gdce',
         'X..X',         'aton',
         '....'),        'qrdi')          -> 'icantforgetiddqd'

        ('....',        ('xhwc',
         'X..X',         'rsqx',
         '.X..',         'xqzz',
         '...X'),        'fyzr')          -> 'rxqrwsfzxqxzhczy'
    """
    text = ""
    num = 0
    while num < 4:
        text += decode_part_text(encrypted_data=encrypted_data,
                                 ciphered_password=ciphered_password)
        encrypted_data = rotate_tuple_90_degrees(data=encrypted_data)
        num += 1
    return text
