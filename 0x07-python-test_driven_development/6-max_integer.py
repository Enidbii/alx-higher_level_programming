#!/usr/bin/python3
""" 6-max integer module """


def max_integer(list=[]):
    """
        find and returns max int
        if list is empty it returns none
    """
    if len(list) == 0:
        return None
    max_int = list[0]
    j = 1
    while j < len(list):
        if list[j] > max_int:
            max_int = list[j]
        j += 1
    return max_int
