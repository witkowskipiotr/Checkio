import unittest

from code_wars.counting_duplicates import duplicate_count


class CountingDuplicatesTest(unittest.TestCase):

    def test_main_function_counting_duplicates(self):
        self.assertEqual(duplicate_count(text="abcde"), 0)
        self.assertEqual(duplicate_count(text="aabbcde"), 2)
        self.assertEqual(duplicate_count(text="aabBcde"), 2)
        self.assertEqual(duplicate_count(text="indivisibility"), 1)
        self.assertEqual(duplicate_count(text="Indivisibilities"), 2)
        self.assertEqual(duplicate_count(text="aA11"), 2)
        self.assertEqual(duplicate_count(text="ABBA"), 2)
