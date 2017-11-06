import unittest

from code_wars.longest_consec import longest_consec


class LongestConSecTest(unittest.TestCase):

    def test_main(self):

        # test case
        self.assertEqual(longest_consec(
            str_arr=["zone", "abigail", "theta", "form", "libe", "zas"], number_to_connect=2),
            "abigailtheta")
        self.assertEqual(longest_consec(
            str_arr=["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb",
                     "oocccffuucccjjjkkkjyyyeehh"],
            number_to_connect=1),
            "oocccffuucccjjjkkkjyyyeehh")
        self.assertEqual(longest_consec(
            [], 3),
            "")
        self.assertEqual(longest_consec(
            str_arr=["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv",
                     "vweqilsfytihvrzlaodfixoyxvyuyvgpck"],
            number_to_connect=2),
            "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEqual(longest_consec(
            str_arr=["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], number_to_connect=2),
            "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEqual(longest_consec(
            str_arr=["zone", "abigail", "theta", "form", "libe", "zas"], number_to_connect=-2),

            "")
        self.assertEqual(longest_consec(
            str_arr=["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], number_to_connect=3),
            "ixoyx3452zzzzzzzzzzzz")
        self.assertEqual(longest_consec(
            str_arr=["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], number_to_connect=15),
            "")
        self.assertEqual(longest_consec(
            str_arr=["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], number_to_connect=0),
            "")
