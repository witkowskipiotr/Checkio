# -*- coding: utf-8 -*-
"""
empire of code
"""


def reverse_360(degre: float) -> int:
    """If degre is up 180 then calculate inverse angle"""
    return degre if degre < 180 else abs(360 - degre)

def clock_angle(time: str) -> int:
    """
    :param time: time as string
    :return: minimum angle between big and small hands og the clock as integer
    """
    (hour, minute) = time.split(":")
    hour = int(hour) % 12
    hour_angle = float(hour) * 30 + float(minute) / 2
    minute_angle = float(minute) * 6
    result = abs(minute_angle - hour_angle)
    return reverse_360(result)
