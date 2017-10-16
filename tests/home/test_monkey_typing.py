import unittest

from home.monkey_typing import monkey_typing

class CheckioTest(unittest.TestCase):

    def test_monkey_typing_not_equal(self):
        self.assertNotEqual(monkey_typing("How aresjfhdskfhskd you?", {"how"}), 4)

    def test_monkey_typing_equal(self):
        # first argument is a text, second is solution
        self.values = [
            [["How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}], 3],
            [[], 2],
            [["Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                {"sum", "hamlet", "infinity", "anything"}], 1],
        ]
        for value in self.values:
            self.assertEqual(monkey_typing("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}), 3)
            self.assertEqual(monkey_typing("Bananas, give me bananas!!!", {"banana", "bananas"}), 2)
            self.assertEqual(monkey_typing("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                {"sum", "hamlet", "infinity", "anything"}), 1)