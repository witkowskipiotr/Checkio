import unittest

from elementary.digits_multiplication import digits_multiplication


class CheckioTest(unittest.TestCase):

    def test_index_power_not_equal(self):
        self.assertNotEqual(digits_multiplication(number=1), 0)

    def test_index_power_equal(self):
        self.assertEqual(digits_multiplication(number=10), 1)
        self.assertEqual(digits_multiplication(number=101), 1)
        self.assertEqual(digits_multiplication(number=1011), 1)
        self.assertEqual(digits_multiplication(number=1021), 2)
        self.assertEqual(digits_multiplication(number=0000), 0)
