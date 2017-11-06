import unittest

from code_2017_11_06.anagrams import anagrams


class CheckAnagramsWordTest(unittest.TestCase):

    def test_no_anagrams(self):
        self.assertEqual(
            anagrams(key_word='big',
                     words_to_check=['gig', 'dib', 'bid', 'biig']),
            []
        )

    def test_one_anagrams(self):
        self.assertEqual(
            anagrams(key_word='a',
                     words_to_check=['a', 'b', 'c', 'd']),
            ['a']
        )

    def test_all_anagrams(self):
        self.assertEqual(
            anagrams(key_word='abc',
                     words_to_check=['abc', 'acb', 'cba', 'cab']),
            ['abc', 'acb', 'cba', 'cab']
        )

    def test_any_anagrams(self):
        self.assertEqual(
            anagrams(key_word='abba',
                     words_to_check=['aabb', 'abcd', 'bbaa', 'dada']),
            ['aabb', 'bbaa']
        )
        self.assertEqual(
            anagrams(key_word='racer',
                     words_to_check=['crazer', 'carer', 'racar', 'caers', 'racer']),
            ['carer', 'racer']
        )
        # different lenght key_word and words in words_to_check
        self.assertEqual(
            anagrams(key_word='abba',
                     words_to_check=['a', 'b', 'c', 'd', 'aabb', 'bbaa',
                                     'abab', 'baba', 'baab', 'abcd', 'abbba',
                                     'baaab', 'abbab', 'abbaa', 'babaa']),
            ['aabb', 'bbaa', 'abab', 'baba', 'baab']
        )

