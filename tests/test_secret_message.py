# -*- coding: utf-8 -*-
import unittest

from elementary.secret_message import find_message

class CheckioTest(unittest.TestCase):

    def test_find_message_not_equal(self):
        self.assertNotEqual(find_message("How are you? Eh, ok. Low or Lower? Ohhh."), "HEELLO")

    def test_find_message_equal(self):
        self.assertEqual(find_message(["How are you? Eh, ok. Low or Lower? Ohhh."]), None)
        self.assertEqual(find_message("How are you? Eh, ok. Low or Lower? Ohhh."), "HELLO")
        self.assertEqual(find_message(""), "")
        self.assertEqual(find_message("aaaaaaaaaa"), "")
        self.assertEqual(find_message("ABCDEFGK"), "ABCDEFGK")
        self.assertEqual(find_message("ABCDEF   K"), "ABCDEFK")
        self.assertEqual(find_message("".join(str(1) for x in range(1001))), None)
        self.assertEqual(find_message("".join(str(1) for x in range(1000))), "")
        self.assertEqual(find_message("".join(str("d") for x in range(1000))), "")
