import unittest

from elementary.most_number import checkio

class CheckioTest(unittest.TestCase):

    def test_most_number_not_equal(self):
        self.assertNotEqual(checkio(range(21)), 12)
        self.assertNotEqual(checkio(1,2,122), 12)

    def test_most_number_equal(self):
        self.assertEqual(checkio(range(21)), None)
        self.assertEqual(checkio({12: 12}), None)
        self.assertEqual(checkio(120), None)
        self.assertEqual(checkio(), 0)
        self.assertEqual(checkio(12,13,14,22), 10)
