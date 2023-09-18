"""
Testing the Rectangle Class For Error
"""

import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):

    def test_for_constructor(self):
        "Tests for constructors and inheritance from Base"
        r1 = Rectangle(5, 3)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Rectangle)

    def test_for_attributes(self):
        """ Test for private attributes """
        r1 = Rectangle(15, 8)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_for_setter(self):
        """ test for setters """
        r1 = Rectangle(15, 8)
        r1.width = 10
        r1.height = 3
        r1.x = 12
        r1.y = 9
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 9)

    def test_for_invalid_width(self):
        """ Test for invalid width """
        with self.assertRaises(TypeError):
            r1 = Rectangle("String", 3)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 5)

    def test_for_invalid_height(self):
        """ Test for invalid height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, "string")
        with self.assertRaises(ValueError):
            r1 = Rectangle(3, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -1)

    def test_for_invalid_x(self):
        """ Test for invalid x """
        with self.assertRaises(ValueError):
            r1 = Rectangle(3, 4, -1, 7)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 4, "string", 8)

    def test_for_invalid_y(self):
        """ Test for invalid y """
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 3, 4, -5)
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 4, 2, "string")

    def test_for_area(self):
        """ Testing area method in Rectangle """
        r1 = Rectangle(5, 2)
        self.assertEqual(r1.area(), 10)

        r2 = Rectangle(6, 5)
        self.assertEqual(r2.area(), 30)

        r3 = Rectangle(1, 3, 0, 0, 20)
        self.assertEqual(r3.area(), 3)

    def test_for_display(self):
        """ Testing for display """
        r1 = Rectangle(4, 4)
        expected_output = "####\n####\n####\n####\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r2 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r3 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_for_str(self):
        """ Testing for str method in Rectangle Class """
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected_output)

        r2 = Rectangle(3, 4, 1)
        expected_output = "[Rectangle] (24) 1/0 - 3/4"
        self.assertEqual(str(r2), expected_output)

    def test_for_update(self):
        """ Testing for update method """
        r1 = Rectangle(10, 10, 10, 10)
        expected_output = "[Rectangle] (25) 10/10 - 10/10"
        self.assertEqual(str(r1), expected_output)

        r1.update(89)
        expected_output = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(str(r1), expected_output)

        r1.update(89, 2)
        expected_output = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(str(r1), expected_output)

        r1.update(89, 2, 3)
        expected_output = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(str(r1), expected_output)

        r1.update(89, 2, 3, 4)
        expected_output = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(str(r1), expected_output)

        r1.update(89, 2, 3, 4, 5)
        expected_output = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str(r1), expected_output)


if __name__ == "__main__":
    unittest.main()
