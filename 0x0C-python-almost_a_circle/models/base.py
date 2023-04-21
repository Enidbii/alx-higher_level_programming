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
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes json string representation to a file
        Args:
            list_objs: list of instances inherit from base
        """
        if list_objs:
            string = cls.to_json_string([obj.to_dictionary()
                                         for obj in list_objs])
        else:
            string = '[]'
        with open(cls.__name__ + '.json', 'w') as file:
            file.write(string)

    def from_json_string(json_string):
        """
        returns the list of json string
        Args:
            json_string: string representing list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns list pf instances """
        f_name = cls.__name + '.json'
        with open(f_name, 'r') as file:
            dic = cls.from_json_string(file.read())
            return [cls.create(**dictionary) for f in dic]
        except FileNotFoundError:
            return []
