#!/usr/bin/python3
""" 4-print square module """


def print_square(size):
    """
    prints square with the character #

    Args:
        size: size of square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
