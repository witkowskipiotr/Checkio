import unittest

from code_2017_11_06.bouncing_ball import bouncing_ball


class SellTicketTest(unittest.TestCase):

    def test_give_true_value(self):
        self.assertEqual(bouncing_ball(hight=3, bounce=0.66, window=1.5), 3)
        self.assertEqual(bouncing_ball(hight=30, bounce=0.66, window=1.5), 15)
        self.assertEqual(bouncing_ball(hight=30, bounce=0.75, window=1.5), 21)
        self.assertEqual(bouncing_ball(hight=30, bounce=0.4, window=10), 3)
        self.assertEqual(bouncing_ball(hight=35.5, bounce=0.57, window=3.5), 9)
        self.assertEqual(bouncing_ball(hight=57, bounce=0.9, window=0.57), 87)

    def test_aut_of_range(self):
        self.assertEqual(bouncing_ball(hight=3, bounce=0.75, window=3), -1)
        self.assertEqual(bouncing_ball(hight=5, bounce=-1, window=1.5), -1)
        self.assertEqual(bouncing_ball(hight=61, bounce=1.1, window=6.1), -1)
        self.assertEqual(bouncing_ball(hight=15.9, bounce=1, window=1.9), -1)
        self.assertEqual(bouncing_ball(hight=-5, bounce=0.65, window=1.5), -1)
        self.assertEqual(bouncing_ball(hight=40, bounce=1, window=10), -1)
