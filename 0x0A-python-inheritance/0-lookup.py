#!/usr/bin/python3
from pprint import pprint
""" lookup module """


def lookup(obj):
    """ returns list of attributes and methods of obj """
    pprint(dir(obj))
