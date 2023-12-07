#!/usr/bin/python3
""" 3-say-my-name module """


def say_my_name(first_name, last_name=""):
    """
        prints out my name

        Args:
            first_name: first name
            last_name: last name

        Returns:
            My name is <first_name> <last_name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
