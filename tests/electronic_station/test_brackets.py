import unittest

from electronic_station.brackets import checkio


class CheckioTest(unittest.TestCase):

    def test_brackets_into_expresion_open_and_close(self):
        self.assertEqual(checkio("((5+3)*2+1)"), True)
        self.assertEqual(checkio("{[(3+1)+2]+}"), True)
        self.assertEqual(checkio("(3+{1-1)}"), False)
        self.assertEqual(checkio("[1+1]+(2*2)-{3/3}"), True)
        self.assertEqual(checkio("(({[(((1)-2)+3)-3]/3}-3)"), False)
        self.assertEqual(checkio("2+3"), True)
        self.assertEqual(checkio("(((1+(1+1))))]"), False)
