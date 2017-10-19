import unittest

from oreilly.friends import Friends


class CheckioTest(unittest.TestCase):
    def setUp(self):
        self.letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
        self.digit_friends = Friends([{"1", "2"}, {"3", "1"}])

    def test_check_connection_equal(self):
        self.assertFalse(self.letter_friends.check_connection({"c", "d"}))
        self.assertTrue(self.letter_friends.check_connection({"a", "b"}))
        self.assertTrue(self.digit_friends.check_connection({"1", "3"}))

    def test_add_connection_equal(self):
        self.assertTrue(self.letter_friends.add({"c", "d"}))
        self.assertFalse(self.letter_friends.add({"a", "b"}))
        self.assertTrue(self.digit_friends.add({"2", "4"}))
        self.assertFalse(self.digit_friends.add({"2", "1"}))

    def test_remove_connection_equal(self):
        self.assertFalse(self.letter_friends.remove({"c", "d"}))
        self.assertTrue(self.letter_friends.remove({"a", "b"}))
        self.assertFalse(self.digit_friends.remove({"2", "4"}))
        self.assertTrue(self.digit_friends.remove({"2", "1"}))

    def test_names_item_connection_equal(self):
        self.assertEqual(self.letter_friends.names(), {"a", "b", "c"})
        self.assertEqual(self.digit_friends.names(), {"1", "2", "3"})

    def test_connected_item_connection_equal(self):
        self.assertEqual(self.letter_friends.connected("a"), {"b", "c"})
        self.assertEqual(self.digit_friends.connected("3"), {"1"})
