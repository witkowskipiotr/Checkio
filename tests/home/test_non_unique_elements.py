import unittest

from home.non_unique_elements import non_unique_elements


class CheckioTest(unittest.TestCase):

    def test_non_unique_elements_not_equal(self):
        self.assertNotEqual(non_unique_elements([1, 2, 3, 1, 3]), [])

    def test_non_unique_elements_equal(self):
        # first argument is a text, second is solution
        self.values = [
            ([1, 2, 3, 1, 3], [1, 3, 1, 3]),
            ([1, 2, 3, 4, 5], []),
            ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
            ([10, 9, 10, 10, 9, 8], [10, 9, 10, 10, 9]),
        ]
        for value in self.values:
            self.assertEqual(non_unique_elements(value[0]),value[1])
