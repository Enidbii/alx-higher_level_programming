#!/usr/bin/python3
""" My list module """


class MyList(list):
    """ MyList inherits from list """
    def __init__(self):
        """ initialize class mylist """
        super().__init__()

    def print_sorted(self):
        """ prints list in a sorted way """
        return sorted(self)
