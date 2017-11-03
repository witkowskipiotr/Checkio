# -*- coding: utf-8 -*-
"""
Task from
http://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
"""

def longest_consec(str_arr: list, number_to_connect: int) -> str:
    """
    You are given an array str_arr of strings and an integer k (number_to_connect).
    Your task is to return the first longest string consisting
    of k consecutive strings taken in the array.
    Example:
        longest_consec(["zone", "abigail", "theta", "form",
                        "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

    n being the length of the string array, if n = 0 or k > n or k <= 0 return ""
    """
    if not str_arr or number_to_connect > len(str_arr) \
            or number_to_connect <= 0:
        return ""
    result_array = {}
    for iterate in range(len(str_arr) - number_to_connect + 1):
        lenght_of_string_connection = 0
        for text in str_arr[iterate: iterate + number_to_connect]:
            lenght_of_string_connection += len(text)
        if lenght_of_string_connection not in result_array:
            result_array[lenght_of_string_connection] = iterate
    max_lenght_after_connection = max(result_array)
    max_lenght_index_start = result_array[max_lenght_after_connection]
    result = str_arr[max_lenght_index_start: max_lenght_index_start + number_to_connect]
    return "".join(result)
