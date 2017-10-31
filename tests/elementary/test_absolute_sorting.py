import unittest

from elementary.absolute_sorting import absolute_sorting


class CheckioTest(unittest.TestCase):

    def test_absolute_sorting_not_equal(self):
        self.assertNotEqual(absolute_sorting((12, -3, 13, 0)), [0, -3, 12, ])

    def test_absolute_sorting_equal(self):
        self.assertEqual(absolute_sorting((12, -3, 13, 0)), [0, -3, 12, 13])
        self.assertEqual(absolute_sorting((1, 2, 3, 0)), [0, 1, 2, 3])
        self.assertEqual(absolute_sorting((-1, -2, -3, 0)), [0, -1, -2, -3])
        self.assertEqual(absolute_sorting((-20, -5, 10, 15)), [-5, 10, 15, -20])
