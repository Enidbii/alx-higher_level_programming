#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_negative(self):
        """ 
        checks if the function can come up with
        highest negative integer
        """
        self.AssertEqual(max_integer([-4, -5,-6], -1)

