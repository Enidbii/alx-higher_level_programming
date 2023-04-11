#!/usr/bin/python3
""" square module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle class """
    def __init__(self, size):
        """ initialises the square class
        Args:
            size: size of square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ returns area """
        super().area()

    def __str__(self):
        """ string representation of clas square """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
