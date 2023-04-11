#!/usr/bin/python3r
""" Base Geometry module """


class BaseGeometry:
    """ Base Geometry class """
    def __init__(self):
        pass

    def area(self):
        """ solve area """
        raise Exception("area not implemented")

    def integer_validator(self, name, value):
        """
        validates value
         Args:
            name: of integer
            value: value of validated
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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
        return "[Rectangle] {:d}/{:d}".format(self.width, self.height)
