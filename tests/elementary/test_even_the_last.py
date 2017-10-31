import unittest

from elementary.even_the_last import checkio


class CheckioTest(unittest.TestCase):

    def test_most_number_not_equal(self):
        self.assertNotEqual(checkio([0, 1, 2, 3, 4, 5]), 30 + 1)
        self.assertNotEqual(checkio([1, 3, 5]), 30 + 1)
        self.assertNotEqual(checkio([6]), 36 + 1)
        self.assertNotEqual(checkio([]), 0 + 1)

    def test_most_number_equal(self):
        self.assertEqual(checkio([0, 1, 2, 3, 4, 5]), 30)
        self.assertEqual(checkio([1, 3, 5]), 30)
        self.assertEqual(checkio([6]), 36)
        self.assertEqual(checkio([]), 0)
