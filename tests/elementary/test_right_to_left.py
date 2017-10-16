import unittest

from elementary.right_to_left import right_to_left

class CheckioTest(unittest.TestCase):

    def test_index_power_not_equal(self):
        self.assertNotEqual(right_to_left(("left", "right", "left", "stop")), "ds")

    def test_index_power_equal(self):
        self.assertEqual(right_to_left(phrases=("left", "right", "left", "stop")),
                         "left,left,left,stop")
        self.assertEqual(right_to_left(phrases=("bright aright", "ok")), "bleft aleft,ok")
        self.assertEqual(right_to_left(phrases=("brightness wright",)), "bleftness wleft")
        self.assertEqual(right_to_left(phrases=("enough", "jokes")), "enough,jokes")
