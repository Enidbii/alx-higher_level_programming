#!/usr/bin/python3
""" class inheritance """


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: super class
        a_class: specified class
        returns true if instance of class and false
        if otherwise
    """
    return isinstance(obj, a_class)
