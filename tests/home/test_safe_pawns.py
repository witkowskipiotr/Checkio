import unittest

from home.pawn_brotherhood import *


class CheckioTest(unittest.TestCase):

    def test_find_key_equal(self):
        self.data = {'key1': 'value1', 'key2': 'value2'}
        self.assertEqual(find_key(self.data, 'value2'), 'key2')

    def test_safe_pawns_equal(self):
        self.assertEqual(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}), 6)
        self.assertEqual(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}), 1)
        self.assertEqual(safe_pawns({"b4", "a3"}), 1)
        self.assertEqual(safe_pawns({"b4"}), 0)
        self.assertEqual(safe_pawns({}), 0)
