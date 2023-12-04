#!/usr/bin/python3
""" inherits from class module """


def inherits_from(obj, a_class):
    """
    instance of object
    Args:
        obj: super class
        a_class: specified class
    Returns: true if instance inherits from
            class and false otherwise
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
