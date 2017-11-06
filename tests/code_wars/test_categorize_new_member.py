import unittest

from code_wars.categorize_new_member import check_categorize, open_or_senior


class LongestConSecTest(unittest.TestCase):

    def test_main_open_or_senior(self):
        self.assertEqual(open_or_senior(data=[[45, 12], [55, 21], [19, -2], [104, 20]]),
                         ['Open', 'Senior', 'Open', 'Senior'])
        self.assertEqual(open_or_senior(data=[[16, 23], [73, 1], [56, 20], [1, -1]]),
                         ['Open', 'Open', 'Senior', 'Open'])

    def test_check_categorize_membership(self):
        self.assertEqual(check_categorize(old=74, handicap=13), 'Senior')
        self.assertEqual(check_categorize(old=100, handicap=7), 'Open')
        self.assertEqual(check_categorize(old=100, handicap=3), 'Open')
        self.assertEqual(check_categorize(old=22, handicap=26), 'Open')
        self.assertEqual(check_categorize(old=54, handicap=8), 'Open')
        self.assertEqual(check_categorize(old=55, handicap=7), 'Open')
        self.assertEqual(check_categorize(old=55, handicap=8), 'Senior')
        self.assertEqual(check_categorize(old=55, handicap=-8), 'Senior')
