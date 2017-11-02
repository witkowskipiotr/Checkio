# -*- coding: utf-8 -*-
"""
O'Reilly functions from https://py.checkio.org/mission/ghosts-age/
"""


def fibonaci_generator(number: int):
    """
    Slave generator - called in function:
        - ghost_age
    In mathematics, the Fibonacci numbers are the numbers in the following integer sequence,
    called the Fibonacci sequence, and characterized by the fact that every number after
    the first two is the sum of the two preceding ones.
    Defined:
        F(n)=F(n-1)+F(n-2)
    Example:
        number = 0
        value: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
        F(0) = 0, F(2) = 1, F(7) = 13, F(9) = 34
        fibonaci_generator = fibonaci(0)
        number = next(fibonaci_generator) -> number = 0
    Args:
        number: The first element of the list of int
    Return:
        Next value of fibonacci sequence (int)
    """
    first, second = number, number + 1
    while True:
        yield first
        first, second = second, first + second


def ghost_age(opaque: int) -> bool:
    """
    Main function
    The function checks the age of the ghosts. Age is associated with opaque.
     The new spirit has a opaque of 10000 on a scale of 0 to 10000.
     Opaque is related to age, in every year of life the spirit of his opaque:
     if a given year is a number of fibonacci, we subtract opacity by the amount of this year
     if it is not a number of fibonacci its opaque increases by 1.
    example:
        opaque = 9990
        A newborn ghost -- 10000 units of opacity.
        1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
        2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).
        3 year -- 9997 - 3 = 9994 (3 is a Fibonacci number).
        4 year -- 9994 + 1 = 9995 (4 is not a Fibonacci number).
        5 year -- 9995 - 5 = 9990 (5 is a Fibonacci number).
        return 5
    Args:
        opaque: An opacity measurement as an integer
    return:
        The age of the ghost as an integer
    """
    fibonaci = fibonaci_generator(number=1)
    age_ghost = 0
    opaque_actual = 10000
    is_fib = True
    while True:
        if age_ghost > 5000:
            # if ghost_age is more than 5000 return
            return None
        if opaque == opaque_actual:
            return age_ghost
        age_ghost += 1
        if is_fib:
            fib = next(fibonaci)
        if age_ghost == fib:
            opaque_actual -= fib
            is_fib = True
        elif age_ghost != fib:
            opaque_actual += 1
            is_fib = False
