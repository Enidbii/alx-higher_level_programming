#!/usr/bin/python3
""" is_same_class module """


def is_same_class(obj, a_class):
    """
    Args:
        obj: super class
        a_class: specified class
    Return: True if exactlyinstance and false otherwise
    """
    if (isinstance(obj, a_class) is True):
        return True
    else:
        return False
