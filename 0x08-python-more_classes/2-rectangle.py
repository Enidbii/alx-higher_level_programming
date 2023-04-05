#!/usr/bin/python3
""" defines a class rectangle """


class Rectangle:
    """ class rectangle """
    def __init__(self, width=0, height=0):
        """
        initialises class rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieves the width of rectangle """
        self.__width = width

    @width.setter
    def width(self, value):
        """ setter for the width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ gets the height of the rectangle """
        self.__height = height

    @height.setter
    def height(self, value):
        """ sets height for the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height =value
    
    def area(self):
        """ returns area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of the rectangle """
        if width == 0 and height == 0:
            self.perimeter = 0
        else:
            return 2 * (self.__width + self.__height)
