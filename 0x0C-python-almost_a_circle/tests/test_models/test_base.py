#!/usr/bin/python3

import unittest

import models.base



class TestBase(unittest.TestCase):
    """ test the integer validator """
    def test_integer_validator(self, name, value):
        with self.assertRaises(TypeError):
            integer_validator("width", "2")
            integer_validator("height", 10)
            integer_validator("width", -1)
            
        with self.assertRaises(ValueError):
            integer_validator("width", -10)
            integer_validator("height", 10)

    def test_second_validator(self, name, value):
        with self.assertRaises(TypeError):
            second_validator("x", 3)
            second_validator("y", -2)
            second_validator("x", 0.5)
            second_validator("x", "4")

        with self.assertRaises(ValueError):
            second_validator("x", -20)
            second_validator("y", "2")
            second_validator("x", 10)
            second_validator("y", -1)

if __name__ == "__main__":
    unittest.main()
