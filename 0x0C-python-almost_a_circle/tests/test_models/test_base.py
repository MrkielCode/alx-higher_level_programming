"""
This is a unit test for base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for Base case
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_default_id(self):
        """ Testing for default id """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """ Testing custom id """
        b4 = Base(10)
        self.assertEqual(b4.id, 10)

    def test_mixed_id(self):
        """ Testing for custom and mixed id """
        b5 = Base()
        b6 = Base(30)
        b7 = Base()
        self.assertEqual(b5.id, 1)
        self.assertEqual(b6.id, 30)
        self.assertEqual(b7.id, 2)

    def test_for_empty_json(self):
        """ testing when an empty string is pass """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_for_none_json(self):
        """ testing for none json """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_for_json_string_single_dict(self):
        """ testing for passing dict """
        dict_1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        result = Base.to_json_string([dict_1])
        expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(result, expected)

    def test_for_json_string_multi_dicts(self):
        """ testing for multiple dictionary """
        dict_1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        dict_2 = {'x': 1, 'width': 5, 'id': 2, 'height': 3, 'y': 4}
        result = Base.to_json_string([dict_1, dict_2])
        output = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, '\
            '{"x": 1, "width": 5, "id": 2, "height": 3, "y": 4}]'
        self.assertEqual(result, output)

    @classmethod
    def setUpClass(cls):
        """ Creating a temporary testing file """

        cls.rectangles = [Rectangle(8, 3), Rectangle(4, 2)]
        cls.squares = [Square(5), Square(3)]
        cls.rectangles_filename = "Rectangle.json"
        cls.squares_filename = "Square.json"

    @classmethod
    def tearDownClass(cls):
        """ Removing temp file after testing """
        for filename in [cls.rectangles_filename, cls.squares_filename]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_for_save_rect_file(self):
        """ Testing to save file """
        Rectangle.save_to_file(self.rectangles)
        self.assertTrue(os.path.exists(self.rectangles_filename))

    def test_for_save_rect_file(self):
        """ Testing for save file """
        Square.save_to_file(self.squares)
        self.assertTrue(os.path.exists(self.squares_filename))


if __name__ == "__main__":
    unittest.main
