import unittest

from home.most_wanted_letter import most_wanted_letter


class CheckioTest(unittest.TestCase):

    def test_most_wanted_letter_not_equal(self):
        self.assertNotEqual(most_wanted_letter("Hello World!"), "w")

    def test_most_wanted_letter_equal(self):
        # first argument is a text, second is solution
        self.values = [
            ("Hello World!", "l"),
            ("How do you do?", "o"),
            ("One", "e"),
            ("Oops!", "o"),
            ("AAaooo!!!!", "a"),
            ("abe", "a")
        ]
        for value in self.values:
            self.assertEqual(most_wanted_letter(value[0]),value[1])
