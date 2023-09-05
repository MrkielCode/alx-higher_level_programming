#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class runs a test cases on max integer

    """

    def test_for_ordered_list(self):
        """ Testting foe ordered list of integers."""
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def test_for_unordered_list(self):
        """ Testing for unordered list of integers."""
        unordered_list = [3, 2, 4, 1]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_for_max_at_beginning(self):
        """ Testing for max in begining """
        max_begin = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_begin), 4)

    def test_for_empty_list(self):
        """ Testing for empty list """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_for_empty_string(self):
        """ Testing for empty list """
        self.assertEqual(max_integer(""), None)

    def test_for_list_of_string(self):
        """ test for list of string"""
        list_string = ["banana", "apple", "orange", "mango"]
        self.assertEqual(max_integer(list_string), "orange")

    def test_for_string(self):
        """ Testing for string """
        string = "ikechukwu"
        self.assertEqual(max_integer(string), "w")

    def test_for_floats_and_integer(self):
        """Testing for float and integer."""
        floats_and_ints = [1.1, -3.2, 4.5, 15.3, 7.0]
        self.assertEqual(max_integer(floats_and_ints), 15.3)

    def test_for_floats(self):
        """ Testing foe floats """
        floats = [1.0, -2.33, 0.455, 4.2]
        self.assertEqual(max_integer(floats), 4.2)

    def test_for_single_elem(self):
        """ Test for single elements """
        single = [5]
        self.assertEqual(max_integer(single), 5)


if __name__ == '__main__':
    unittest.main()
