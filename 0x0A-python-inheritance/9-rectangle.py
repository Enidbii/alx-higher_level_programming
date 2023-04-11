#!/usr/bin/python3
""" Base Geometry module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """
        Initializing function
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ informal string representation of rectangle """
        str1 = "[" + str(self.__class__.__name__) + "] "
        str1 += str(self.__width) + "/" + str(self.__height)
        return str1
