#!/usr/bin/python3

""" Suare module """

class Square:

    """ Initiatizing init with try """
    
    def __init(self, size = 0):
        self.__size = size
        try:
            Square()
        except TypeError:
            raise size must be an integer
        except ValueError:
            if size < 0:
                raise size must be >= 0
