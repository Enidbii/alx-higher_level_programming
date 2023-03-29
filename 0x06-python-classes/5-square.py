#!/usr/bin/python3
""" Square module """


class Square:
    """ declaring and defining class attributes """
    def __init__(self, size=0) -> None:
        """
        Initializes class attributes

        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """ method to retrieve size of square """
        self.__size = size

    @size.setter
    def size(self, value):
        """
        method to set value of the size of square

        Args:
            value: size of square that can vary
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ method to find area from the value set """
        return self.__size ** 2

    def my_print(self):
        """ method that prints a square using # """
        if self.__size == 0:
            print()
        else:
            i = 0
            while i < self.__size:
                j = 0
                while j < self.__size:
                    print("{}".format("#"), end='')
                    j += 1
                print()
                i += 1
