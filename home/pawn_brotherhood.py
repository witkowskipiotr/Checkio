# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/pawn-brotherhood/
"""


def find_key(input_dict, value):
    """search dictionary by value - return key"""
    return next((key for key, val in input_dict.items() if val == value), None)


def safe_pawns(pawns: set) -> int:
    """
    A pawn is generally a weak unit, but we have 8 of them which we can use to build
    a pawn defense wall. With this strategy, one pawn defends the others.
    A pawn is safe if another pawn can capture a unit on that square.
    We have several white pawns on the chess board and only white pawns.
    You should design your code to find how many pawns are safe.
    :param pawns: Placed pawns coordinates as a set of strings.
    :return: The number of safe pawns as a integer.
    """
    horizontal = {alfa:num for alfa, num in zip("abcdefgh", range(1, 9))}
    pawns_safe = 0
    for pawn_current in pawns:
        pawn_can_safe = []
        pos_y_safe = str(int(pawn_current[1])-1)
        pos_x = horizontal[pawn_current[0]]
        if pos_x > 1:
            pos_x_safe = pos_x - 1
            pawn_can_safe.append(str(find_key(horizontal, pos_x_safe)) + pos_y_safe)
        if pos_x < 8:
            pos_x_safe = pos_x + 1
            pawn_can_safe.append(str(find_key(horizontal, pos_x_safe)) + pos_y_safe)
        for pawn_other in pawns:
            if pawn_other in pawn_can_safe:
                pawns_safe += 1
                pawn_can_safe = []
    return pawns_safe
