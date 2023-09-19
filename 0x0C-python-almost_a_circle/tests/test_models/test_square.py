"""
This is a unittest for square class

"""

import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_for_constructors(self):
        """ Testing for constructors """
        s1 = Square(5)
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(5, 3, 2, 10)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 10)

    def test_for_str(self):
        """ Testing for str method """
        s1 = Square(5, 3, 2, 1)
        expected_output = "[Square] (1) 3/2 - 5"
        self.assertEqual(str(s1), expected_output)

        s2 = Square(2, 0, 0, 4)
        expected_output = "[Square] (4) 0/0 - 2"
        self.assertEqual(str(s2), expected_output)

    def test_for_area(self):
        """ Testing for Area """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def testing_for_updates(self):
        """ Testing for update method """

        s1 = Square(5)
        expected_output = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(s1), expected_output)

        s1.update(10)
        expected_output = "[Square] (10) 0/0 - 5"
        self.assertEqual(str(s1), expected_output)

        s1.update(1, 2)
        expected_output = "[Square] (1) 0/0 - 2"
        self.assertEqual(str(s1), expected_output)

        s1.update(1, 2, 3)
        expected_output = "[Square] (1) 3/0 - 2"
        self.assertEqual(str(s1), expected_output)

        s1.update(1, 2, 3, 4)
        expected_output = "[Square] (1) 3/4 - 2"
        self.assertEqual(str(s1), expected_output)

        s1.update(x=12)
        expected_output = "[Square] (1) 12/4 - 2"
        self.assertEqual(str(s1), expected_output)

        s1.update(size=7, y=1)
        expected_output = "[Square] (1) 12/1 - 7"
        self.assertEqual(str(s1), expected_output)

        s1.update(size=7, id=89, y=1)
        expected_output = "[Square] (89) 12/1 - 7"
        self.assertEqual(str(s1), expected_output)

    def test_for_to_dictionary(self):
        """ Testing for dictionary """
        s1 = Square(10, 2, 1)
        expected_output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected_output)

        s2 = Square(10, 2, 1, 1)
        expected_output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected_output)


if __name__ == "__main__":
    unittest.main
