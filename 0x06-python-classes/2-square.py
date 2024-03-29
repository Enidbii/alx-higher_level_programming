#!/usr/bin/python3
""" Square module """


class Square:
    """ defines a  class square """
    def __init__(self, size=0) -> None:
        """
        This is the initialization method

        Args:
        size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
