# -*- coding: utf-8 -*-
import ipdb
"""
electronic station
https://py.checkio.org/mission/brackets/
"""


def checkio(expression):
    """
    :param expression: An expression with different of types
    brackets as a string (unicode)
    :return: A verdict on the correctness of the expression
    in boolean (True or False).
    """
    ipdb.set_trace()
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


a = checkio("(((1+(1+1))))]")
print(a)