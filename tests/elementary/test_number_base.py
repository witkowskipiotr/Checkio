import unittest

from elementary.number_base import number_base

class CheckioTest(unittest.TestCase):

    def test_number_base_not_equal(self):
        self.assertNotEqual(number_base("AF", 16), 1)

    def test_number_base_equal(self):
        self.assertEqual(number_base("AF", 16), 175)
        self.assertEqual(number_base("101", 2), 5)
        self.assertEqual(number_base("101", 5), 26)
        self.assertEqual(number_base("Z", 36), 35)
        self.assertEqual(number_base("AB", 10), -1)
