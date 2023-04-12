#!/usr/bin/python3
""" Student class module """


class Student:
    """ student class """
    def __init__(self, first_name, last_name, age):
        """
        initialises cLass student
        Args:
            first_name: student fisrt name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of student """
        return self.__dict__
