#!/usr/bin/python3
""" Base class module """

import json


class Base:
    """base of all other classes of the projects """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        base class constructor
        Args:
            id: id instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    
    def integer_validator(self, name, value):
        """
        validates value
        Args:
            name: of integer
            value: value of validated
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def second_validator(self, name, value):
        """
        validates value 2
        Args:
            name: type
            value: type validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json string representation of listdictionaries
        Args:
            list_dictionaries: list of dictionaries
        """
        list_dictionaries = Base.Rectangle.__init__
        if list_dictionaries is None:
            return "[]"
        return json.loads(list_dictionaries)
