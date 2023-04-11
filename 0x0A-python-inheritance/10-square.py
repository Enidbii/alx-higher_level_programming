#!/usr/bin/python3
"""square module """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from class rectangle """

    def __init__(self, size):
        """ initialise square class
        Args:
            size: size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ returns area of square """
        return self.__size ** 2
