#!/usr/bin/python3
""" My list module """


class MyList(list):
    """ MyList inherits from list """

    def print_sorted(self):
        """ prints list in a sorted way """
        print(sorted(self)
