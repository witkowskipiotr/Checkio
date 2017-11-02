# -*- coding: utf-8 -*-
"""
electronic station
https://py.checkio.org/mission/brackets/
"""


def checkio(expression):
    """
    function  chcecks if brackets in expresion are closedd correctly

    :param expression: An expression with different of types
    brackets as a string (unicode)
    :return: A verdict on the correctness of the expression
    in boolean (True or False).
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
