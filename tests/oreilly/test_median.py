import unittest

from oreilly.median import median

class CheckioTest(unittest.TestCase):

    def test_median_function_equal(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([3, 1, 2, 5, 3]), 3)
        self.assertEqual(median([1, 300, 2, 200, 1]), 2)
        self.assertEqual(median([3, 6, 20, 99, 10, 15]), 12.5)