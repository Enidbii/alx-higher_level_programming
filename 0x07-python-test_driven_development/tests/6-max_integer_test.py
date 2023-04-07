#!/usr/bin/python3
""" Unittest for max_integer([..]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ TestMaxInteger class """
    def test_negative(self):
        """
        checks if the function can come up with
        highest negative integer
        """
        self.AssertEqual(max_integer([-4, -5, -6], -1))

    def test_char(self):
        """ checks for a list of strings """
        self.AssertEqual(max_integer(['e', 'r', 't'], 'k'))

    def test_positive(self):
        """ function to come up with the highest positive int """
        self.AssertEqual(max_integer([1, 2, 3, 4], 4))

    def test_negativefloat(self):
        """ highest float in the list """
        self.AssertEqual(max_integer([-1.34, -2.43, -3.53], -1.34))

    def test_positivefloat(self):
        """ function for positive max integer """
        self.AssertEqual(max_integer([4.33, 2.43, 3.53], 4.33))


if __main__ = '__name__':
    unittest.main()
