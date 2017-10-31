import unittest

from elementary.three_words import three_words


class CheckioTest(unittest.TestCase):

    def test_three_words_not_equal(self):
        self.assertFalse(three_words("Hello World2 hello"))
        self.assertFalse(three_words("1 2 3"))
        self.assertFalse(three_words(""))

    def test_three_words_equal(self):
        self.assertTrue(three_words("a sdf  sfas"))
        self.assertTrue(three_words("sfaS 4 fasd s sf sdfas 44 sf s"))
        self.assertTrue(three_words("1 2 3 4 df sdf sd 3 "))
        self.assertTrue(three_words("1 2 3 4 df sdf sd 3 "))

    def test_three_words_raise(self):
        self.assertRaises(TypeError, three_words)
        self.assertRaises(AttributeError, three_words, [1])
