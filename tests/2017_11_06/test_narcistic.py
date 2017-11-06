import unittest

from code_2017_11_06.narcistic import narcissistic


class NarcissisticNumberTest(unittest.TestCase):

    def test_small_numbers_narcissistic(self):
        self.assertTrue(narcissistic(value=1))
        self.assertTrue(narcissistic(value=5))
        self.assertTrue(narcissistic(value=7))

    def test_larger_numbers_narcissistic(self):
        self.assertTrue(narcissistic(value=153))
        self.assertTrue(narcissistic(value=370))
        self.assertTrue(narcissistic(value=371))
        self.assertTrue(narcissistic(value=1634))

    def test_not_find_numbers_narcissistic(self):
        self.assertFalse(narcissistic(value=266969))
        self.assertFalse(narcissistic(value=797745))
        self.assertFalse(narcissistic(value=310258))
        self.assertFalse(narcissistic(value=532170))
        self.assertFalse(narcissistic(value=528384))
