import unittest

from elementary.index_power import index_power

class CheckioTest(unittest.TestCase):

    def test_index_power_not_equal(self):
        self.assertNotEqual(index_power(table=[1,2], num=4), 8)

    def test_index_power_equal(self):
        self.assertEqual(index_power(table=[1, 2, 3, 4], num=2), 9)
        self.assertEqual(index_power(table=[1, 3, 10, 100], num=3), 1000000)
        self.assertEqual(index_power(table=[0, 1], num=0), 1)
        self.assertEqual(index_power(table=[1, 2], num=3), -1)

    def test_index_power_raise(self):
        self.assertRaises(TypeError,index_power)
        self.assertRaises(TypeError,index_power,[1],[1])
        self.assertRaises(TypeError,index_power,[1, "sd"],[1])
