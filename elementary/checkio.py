"""Simple functions from https://py.checkio.org/"""

def fizz_buzz(number: int) -> str:
    """
    We give positive integer and return string:
    "Fizz Buzz" if the number is divisible by 3 and by 5;
    "Fizz" if the number is divisible by 3;
    "Buzz" if the number is divisible by 5;
    The number as a string for other cases.
    """
    if number <= 0 or number > 1000:
        return ""
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return str(number)
