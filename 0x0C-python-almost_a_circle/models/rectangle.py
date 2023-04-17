#!/usr/bin/python3
""" rectangle module """

from models.base import Base


class Rectangle(Base):
    """ Rectaangle shape """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor of the rectangle class
        Args:
            width: width of rectangle
            height: height of rectangle
            x: x
            y: y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ gets width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of the width """
        self.integer_validator("name", value)
        self.__width = value

    @property
    def height(self):
        """ gets height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height of rectangle """
        self.integer_validator("name", value)
        self.__height = value

    @property
    def x(self):
        """ gets x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets value x """
        self.second_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ gets y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y """
        self.second_validator("y", value)
        self.__y = value

    def area(self):
        """ gets the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints # rectangle """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))
