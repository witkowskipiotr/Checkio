import unittest

from oreilly.days_between import number_days_between_date

class CheckioTest(unittest.TestCase):

    def test_diff_days_equal(self):
        self.assertEqual(number_days_between_date(date1=(1982, 4, 19), date2=(1982, 4, 22)), 3)
        self.assertEqual(number_days_between_date(date1=(2014, 1, 1), date2=(2014, 8, 27)), 238)
        self.assertEqual(number_days_between_date(date1=(2014, 8, 27), date2=(2014, 1, 1)), 238)
        self.assertEqual(number_days_between_date(date1=(2014, 8, 27), date2=(2014, 8, 27)), 0)
        self.assertEqual(number_days_between_date(date1=(1111, 1, 1), date2=(9999, 12, 31)), 3246640)
        self.assertEqual(number_days_between_date(date1=(1, 1, 1), date2=(9999, 12, 31)), 3652058)
        self.assertRaises(ValueError, number_days_between_date, date1=(2017, 2, 20), date2=(2017, 2, 30))
