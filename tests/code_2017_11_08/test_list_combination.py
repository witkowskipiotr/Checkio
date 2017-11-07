import unittest

from code_2017_11_08.list_combination import list_combination


class ListCombinationTest(unittest.TestCase):

    def test_list_combination_good_value(self):
        self.assertEqual(
            list_combination(first_list=[1, 2, 3],
                             second_list=[4, 5, 6]),
            [1, 4, 2, 5, 3, 6])
        self.assertEqual(
            list_combination(first_list=[1, 1, 1, 1],
                             second_list=[2, 2, 2, 2]),
            [1, 2, 1, 2, 1, 2, 1, 2])

    def test_list_combination_bad_value(self):
        # function zip get only value by the same index of list
        self.assertEqual(
            list_combination(first_list=[1, 2], second_list=[]),
            []
        )