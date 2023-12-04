#!/usr/bin/python3
""" is_same_class module """


def is_same_class(obj, a_class):
    """
    Args:
        obj: super class
        a_class: specified class
    Return: True if exactlyinstance and false otherwise
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
