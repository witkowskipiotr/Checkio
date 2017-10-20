import unittest

from oreilly.long_non_repeat import non_repeat

class CheckioTest(unittest.TestCase):

    def test_median_function_equal(self):
        assert non_repeat('aaaaa') == 'a', "First"
        assert non_repeat('abdjwawk') == 'abdjw', "Second"
        assert non_repeat('abcabcffab') == 'abcf', "Third"
        assert non_repeat("") == '', "Empty"
        assert non_repeat("w") == 'w', "lonely"
        assert non_repeat("wq") == 'wq'
        assert non_repeat("abcbde") == 'cbde', "comeon..."