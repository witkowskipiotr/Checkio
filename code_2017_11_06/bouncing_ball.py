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
        bouncing_ball(hight=3, bounce=0.66, 1.5) -> 3
        bouncing_ball(30, 0.66, 1.5) -> 15
    """
    def validate_data():

        """function responsible for checking data correction from funciton boucing ball"""
        height_is_less_than_window = hight <= 0 or hight <= window
        bounce_factor_is_not_correct = bounce >= 1 or bounce <= 0
        if height_is_less_than_window or bounce_factor_is_not_correct:
            return True

    # 1. check if values are correct
    errors = validate_data()
    if errors:
        return -1

    # 2. calculate bounces when mother can see ball
    result = 0
    while True:
        if hight <= window:
            return result
        hight *= bounce
        result += 1
        if hight > window:
            result += 1
