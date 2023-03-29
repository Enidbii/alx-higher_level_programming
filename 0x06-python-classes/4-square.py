#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares class attibutes """
    def __init__(self, size=0) -> None:
        """
        Initialises class attributes

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
        """
        decleares and defines this method's attributes"
        
        Args:
            area: area of the square
        """
        area = self.__size * self.__size
        return area
