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
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ area of rectangle """
        return self__width * self__height

    def __str__(self):
        """ informal string representation of rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
