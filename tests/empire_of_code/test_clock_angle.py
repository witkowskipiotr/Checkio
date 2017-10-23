import unittest

from empire_of_code.clock_angle import clock_angle, reverse_360


class CheckioTest(unittest.TestCase):
    def test_reverse_360(self):
        self.assertEqual(reverse_360(105), 105)
        self.assertEqual(reverse_360(159), 159)
        self.assertEqual(reverse_360(159), 159)
        self.assertEqual(reverse_360(153.5), 153.5)
        self.assertEqual(reverse_360(0), 0)
        self.assertEqual(reverse_360(5.5), 5.5)
        self.assertEqual(reverse_360(180), 180)
        self.assertEqual(reverse_360(200), 160)
        self.assertEqual(reverse_360(205), 155)
        self.assertEqual(reverse_360(185), 175)

    def test_clock_angle(self):
        self.assertEqual(clock_angle("02:30"), 105)
        self.assertEqual(clock_angle("13:42"), 159)
        self.assertEqual(clock_angle("01:42"), 159)
        self.assertEqual(clock_angle("01:43"), 153.5)
        self.assertEqual(clock_angle("00:00"), 0)
        self.assertEqual(clock_angle("12:01"), 5.5)
        self.assertEqual(clock_angle("18:00"), 180)