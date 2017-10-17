import unittest

from home.min_and_max import min as min_val
from home.min_and_max import max as max_val

class CheckioTest(unittest.TestCase):

    def test_min_value_equal(self):
        self.assertEqual(min_val(3, 2), 2)
        self.assertEqual(min_val("hello"), "e")
        self.assertEqual(min_val([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]), [9, 0])

    def test_max_value_equal(self):
        self.assertEqual(max_val(3, 2), 3)
        self.assertEqual(max_val([1, 2, 0, 3, 4]), 4)
        self.assertEqual(max_val(2.2, 5.6, 5.9, key=int), 5.6)
        self.assertEqual(max(True, False, -1, key=lambda x: not x), False)
