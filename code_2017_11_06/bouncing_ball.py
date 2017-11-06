# -*- coding: utf-8 -*-
"""
Task from
http://www.codewars.com/kata/bouncing-balls/train/python
"""


def bouncing_ball(*, hight: float, bounce: float, window: float) -> int:
    """
    A child plays with a ball on the nth floor of a big building.
    The height of this floor is known. He lets out the ball.
    The ball bounces for example to two-thirds of its height.
    His mother looks out of a window that is 1.5 meters from the ground.
    Args:
        hight: the height of which the ball falls
        bounce: Factor to reduce the height of the ball as a result of reflection
        window: the height of the observer
    Return: How many times will the mother see the ball either
            falling or bouncing in front of the window.
    For example:
        bouncing_ball(3, 0.66, 1.5) -> 3
        bouncing_ball(30, 0.66, 1.5) -> 15
    """
    if hight <= 0 or hight <= window:
        return -1
    if bounce >= 1 or bounce <= 0:
        return -1

    result = 0
    while True:
        if hight <= window:
            return result
        hight *= bounce
        result += 1
        if hight > window:
            result += 1
