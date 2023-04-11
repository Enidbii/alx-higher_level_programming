#!/usr/bin/python3
""" lookup module """


def lookup(obj):
    """
    Args:
        obj: Super object
    Returns: list of attributes and methods of obj
    """
    return dir(obj)
