import unittest

from oreilly.ghost_age import ghost_age


class CheckioTest(unittest.TestCase):

    def test_ghost_age(self):
        assert ghost_age(10000) == 0, "Newborn"
        assert ghost_age(9999) == 1, "1 year"
        assert ghost_age(9997) == 2, "2 years"
        assert ghost_age(9994) == 3, "3 years"
        assert ghost_age(9995) == 4, "4 years"
        assert ghost_age(9990) == 5, "5 years"
