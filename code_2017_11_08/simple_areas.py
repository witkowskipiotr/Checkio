# -*- coding: utf-8 -*-
"""
Task Simple Areas
"""

from math import pi, sqrt


def simple_areas(*args) -> float:
    """
    Function calculate the area of simple figures: circles, rectangles and triangles.
    You are given an arbitrary number of arguments which the function
    should use to calculate the area for the different figures.
    One argument -- The diameter of a circle and you need calculate the area of the circle.
    Two arguments -- The side lengths of a rectangle and you need calculate the area of the rectangle.
    Three arguments -- The lengths of each side on a triangle and you need calculate the area of the triangle.
    The result should be given with two digit precision like so: +-0.01
    """
    """
simple_areas(3) == 7.07
simple_areas(2, 2) == 4
simple_areas(2, 3) == 6
simple_areas(3, 5, 4) == 6
simple_areas(1.5, 2.5, 2) == 1.5
    """
    is_too_many_arguments = len(args) > 3
    is_too_small_arguments = not args
    if is_too_many_arguments or is_too_small_arguments:
        return 0

    if len(args) == 1:
        result = pi * (args[0] / 2) ** 2

    elif len(args) == 2:
        result = args[0] * args[1]
    else:
        # pattern Heron
        # half_circuit = (a + b + c) / 2
        # where a, b, c - side triangle
        # area_triangle = sqrt(half_circuit*(half_circuit-a)*(half_circuit-b)*(half_circuit-c))
        half_circuit = sum(args) / 2
        area_triangle = sqrt(half_circuit *
                             (half_circuit - args[0]) * (half_circuit - args[1]) * (half_circuit - args[2])
                             )
        result = area_triangle
    return round(result, 2)
