import unittest

from oreilly.create_intervals import get_sets_of_unbroken_numbers


class CheckioTest(unittest.TestCase):

    def test_check_connection_equal(self):
        self.assertEqual(get_sets_of_unbroken_numbers({1, 2, 3, 4, 5, 7, 8, 12}), [(1, 5), (7, 8), (12, 12)])
        self.assertEqual(get_sets_of_unbroken_numbers({1, 2, 3, 6, 7, 8, 4, 5}), [(1, 8)])
