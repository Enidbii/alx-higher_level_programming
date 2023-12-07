#!/usr/bin/python3
""" Squrae module """


class Square:
    """ declares a square class """
    def __init__(self, size=0) -> None:
        """ Initializes class attrributes

        Args:
            size: size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ declares and defines area attributes

        Args:
            area: area itself
        """
        self.area = self.__size * self.__size
        return self.area
