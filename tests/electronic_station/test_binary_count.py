import unittest

from electronic_station.binary_count import count_units


class CheckioTest(unittest.TestCase):

    def test_count_units(self):
        self.assertEqual(count_units(4), 1)
        self.assertEqual(count_units(15), 4)
        self.assertEqual(count_units(1), 1)
        self.assertEqual(count_units(1022), 9)
