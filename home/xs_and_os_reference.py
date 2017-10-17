# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/x-o-referee/
"""


def check_slant(data: list) -> str:
    """Check if slant is solved"""
    if data[0][0] == data[1][1] == data[2][2] != "." or\
            data[2][0] == data[1][1] == data[0][2] != ".":
        return data[1][1]
    return "."


def check_vertical(data: list) -> str:
    """Check if vertical is solved"""
    for vertical in range(3):
        if data[0][vertical] \
                == data[1][vertical] \
                == data[2][vertical] \
                != ".":
            return data[0][vertical]
    return "."


def check_horizontal(data: list) -> str:
    """Check if horizont is solved"""
    for horizontal in data:
        if horizontal[0] == horizontal[1] == horizontal[2] != ".":
            return horizontal[0]
    return "."


def xs_and_os_reference(data: list) -> str:
    """
    The game for two players (X and O) who take turns marking the spaces in a 3×3 grid.
    The player who succeeds in placing three respective marks in a horizontal,
    vertical, or diagonal rows (NW-SE and NE-SW) wins the game.
    :param data: A game result as a list of strings
    :return: "X", "O" or "D" as a string
    """
    if check_slant(data) != ".":
        return check_slant(data)
    if check_horizontal(data) != ".":
        return check_horizontal(data)
    if check_vertical(data) != ".":
        return check_vertical(data)
    return "D"
