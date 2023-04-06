#!/usr/bin/python3
""" 0-add_integer module """


def add_integer(a, b=98):
    """
    a function that adds two integers

    Args:
        a: iput integer
        b: input integer

    returns a+b
    """
    if type(a) is not float or type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float or type(b) is not int:
        raise TypeError("b must be an integer")
    a_new, b_new = int(a), int(b)
    return a_new + b_new
