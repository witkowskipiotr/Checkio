import unittest

from home.long_repeat import long_repeat

class CheckioTest(unittest.TestCase):

    def test_long_repeat_equal(self):
        self.assertEqual(long_repeat('sdsffffse'), 4)
        self.assertEqual(long_repeat('ddvvrwwwrggg'), 3)
        self.assertEqual(long_repeat('aa'), 2)
        self.assertEqual(long_repeat(''), 0)
