import unittest

from home.xs_and_os_reference import *

class CheckioTest(unittest.TestCase):

    def test_check_slant_equal(self):
        # NW-SE and NE-SW slant win
        self.assertEqual(check_slant(["X.O", "XX.", "XOX"]), "X")
        self.assertEqual(check_slant(["XOX", "XXO", "..X"]), "X")
        # NW-SE and NE-SW slant draw
        self.assertEqual(check_slant(["OO.", "XOX", "XOX"]), ".")
        self.assertEqual(check_slant(["OOX", "XXO", "..X"]), ".")

    def test_check_vertical_equal(self):
        self.assertEqual(check_vertical(["X.O", "XX.", "XOO"]), "X")
        self.assertEqual(check_vertical(["OO.", "XOX", "XOX"]), "O")
        self.assertEqual(check_vertical(["OOX", "XXO", "..X"]), ".")

    def test_check_horizontal_equal(self):
        self.assertEqual(check_horizontal(["X.O", "XX.", "XOO"]), ".")
        self.assertEqual(check_horizontal(["OO.", "XOX", "XOX"]), ".")
        self.assertEqual(check_horizontal(["OOX", "XXX", "..X"]), "X")

    def test_xs_and_os_reference_equal(self):
        self.assertEqual(xs_and_os_reference(["X.O", "XX.", "XOO"]), "X")
        self.assertEqual(xs_and_os_reference(["OO.", "XOX", "XOX"]), "O")
        self.assertEqual(xs_and_os_reference(["OOX", "XXO", "..X"]), "D")
