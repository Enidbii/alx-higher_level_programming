#!/usr/bin/python3
""" defines a class rectangle """


class Rectangle:
    """ class rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialises class rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieves the width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height for the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ prints out # as of height and width """
        hashstr = ""
        if self.__width != 0 and self.__height != 0:
            hashstr += "\n".join(str(self.print_symbol) * self.__width
                                 for j in range(self.__height))
        return hashstr

    def __repr__(self):
        """ string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ prints out when instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns biggest rectangle based on the area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
