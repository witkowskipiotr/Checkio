import unittest
from code_wars.delete_if_more_than_n_times import delete_if_occurs_more_than_n as main_func


class DeleteNthTest(unittest.TestCase):

    def test_delete_occurrences_of_an_element_if_it_occurs_more_than_n_times(self):
        self.assertEqual(main_func(order=[20, 37, 20, 21], max_element=1),
                         [20, 37, 21])
        self.assertEqual(main_func(order=[1, 1, 3, 3, 7, 2, 2, 2, 2], max_element=3),
                         [1, 1, 3, 3, 7, 2, 2, 2])