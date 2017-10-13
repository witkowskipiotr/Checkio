"""Simple functions from https://py.checkio.org/"""

def checkio(*args: float or int):
    """
    difference max and min number between -100 and 100,
    randam amount args
    """
    if not all(isinstance(x, (int, float)) for x in args):
        return
    elif not args:
        return 0
    if len(args) > 20:
        return
    if not all(-100 < x < 100 for x in args):
        return
    return round(max(args), 3) - round(min(args), 3)
