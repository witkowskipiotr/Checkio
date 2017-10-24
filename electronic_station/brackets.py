# -*- coding: utf-8 -*-
"""
electronic station
https://py.checkio.org/mission/brackets/
"""

def checkio(expression):
    """

    :param expression:
    :return:
    """
    level = []
    for char in expression:
        if char == "(":
            level.append(")")
        elif char == "[":
            level.append("]")
        elif char == "{":
            level.append("}")
        elif char in [")", "]", "}"]:
            if not level:
                return False
            elif level and char != level.pop():
                return False
    return True if not level else False
