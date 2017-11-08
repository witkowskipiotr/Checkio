# -*- coding: utf-8 -*-
"""
Task from
https://py.checkio.org/mission/find-sequence/
"""
import numpy


def mirror_list(matrix: list) -> list:
    matrix_mirror_reflection = []
    for index, part in enumerate(matrix):
        matrix_new_line = []
        for item, element in enumerate(part[::-1]):
            matrix_new_line.append(element)
        matrix_mirror_reflection.append(matrix_new_line)
    return matrix_mirror_reflection


def check_sequence(data: list) -> bool:
    """
    slave function
    check if there is a sequence
    of 4 or more matching digits
    """
    count = 0
    number_old = None
    for number in data:
        if number_old and number_old == number:
            count += 1
        else:
            number_old = number
            count = 1
    return count >= 4


def simple_areas(matrix: list) -> bool:
    """
    main function
    Function get a matrix of NxN (4≤N≤10). Check if there is a sequence
    of 4 or more matching digits. The sequence may be positioned horizontally,
    vertically or diagonally (NW-SE or NE-SW diagonals).
    Args:
        matrix: list of int
    Return:
        True if sequence of 4 or more matching digits in any matrix else False

    """
    horizontal_lenght = len(matrix)
    vertical_lenght = len(matrix[0])
    is_not_valid_matrix = horizontal_lenght != vertical_lenght
    if is_not_valid_matrix:
        return False

    for index, list in enumerate(matrix):
        # vertical
        if check_sequence(list):
            return True

        #horizontal
        horizontal_list = []
        for item in range(horizontal_lenght):
            horizontal_list.append(matrix[item][index])
        if check_sequence(horizontal_list):
            return True

    # diagonally
    data = numpy.array(matrix)
    data_mirror = numpy.array(mirror_list(matrix))



    for index in range(horizontal_lenght):
        # NW-SE direction `\
        list_diagonal = [list for list in data.diagonal(index)]
        list_diagonal_expanded = [list for list in data.diagonal(-index)]

        # NE-SW direction /`
        list_diagonal_mirror = [list for list in data_mirror.diagonal(index)]
        list_diagonal_mirror_expanded = [list for list in data_mirror.diagonal(-index)]

        for to_check in [list_diagonal, list_diagonal_expanded, list_diagonal_mirror, list_diagonal_mirror_expanded]:
            if check_sequence(to_check):
                return True

    return False


