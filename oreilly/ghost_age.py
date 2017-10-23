# -*- coding: utf-8 -*-
"""
Home functions from
https://py.checkio.org/mission/ghosts-age/
"""


def fibonaci(number: int):
    """
    fibonaci generator
    :param n: start number
    :return: next fibonaci value
    """
    first, second = number, number + 1
    while True:
        yield first
        first, second = second, first + second


def ghost_age(opaque: int) -> bool:
    """
    Examination of ghost ages based on opacity
    :param opaque: An opacity measurement as an integer
    :return: The age of the ghost as an integer
    """
    fibonaci_generator = fibonaci(1)
    i = 0
    opaque_actual = 10000
    is_fib = True
    while True:
        if i > 5000:
            return 0
        if opaque == opaque_actual:
            return i

        i += 1
        if is_fib:
            fib = next(fibonaci_generator)
        if i == fib:
            opaque_actual -= fib
            is_fib = True
        elif i != fib:
            opaque_actual += 1
            is_fib = False
