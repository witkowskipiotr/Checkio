# -*- coding: utf-8 -*-
"""
New module with one function to check strength password
"""


import re

def validate_password(*, password: str) -> bool:
    """
    The password will be considered strong enough if its length is greater
    than or equal to 10 characters, it contains at least one digit,
    as well as at least one uppercase letter and one lowercase letter.
    The password may only contain ASCII latin letters or digits,
    no punctuation symbols.
    :return: True if password is valid else False
    For example:
        validate_password(password='A1213pokl') -> False
        validate_password(password='bAse730onE') -> True
        validate_password(password='QwErTy911poqqqq') -> True
    """
    pattern = re.compile(r"(?=[a-zA-Z0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])")
    return bool(re.match(pattern, password)) and len(password) >= 10
