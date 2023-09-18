import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_default_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        b4 = Base(10)
        self.assertEqual(b4.id, 10)

    def test_mixed_id(self):
        """ Test that the id is incremented correctly after custom id """
        b5 = Base()
        b6 = Base(30)
        b7 = Base()
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, 30)
        self.assertEqual(b7.id, 5)

if __name__ == "__main__":
    unittest.main()

