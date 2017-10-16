# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/house-password/
"""


def house_password(password: str) -> bool:
    """
    PThe password will be considered strong enough if its length is greater
    than or equal to 10 symbols, it has at least one digit,
    as well as containing one uppercase letter and one lowercase letter in it.
    :param password: A password as a string
    :return: Is the password safe or not as a boolean or any data type
    that can be converted and processed as a boolean.
    In the results you will see the converted results
    """
    if len(password) < 10:
        return False
    graduade_pass = [False, False, False]
    for char in password:
        if char.isupper():
            graduade_pass[0] = True
        elif char.islower():
            graduade_pass[1] = True
        elif char.isdigit():
            graduade_pass[2] = True
    return False not in graduade_pass
