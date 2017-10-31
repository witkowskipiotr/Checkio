import unittest

from oreilly.boolean_algebra import *


class CheckioTest(unittest.TestCase):
    def setUp(self):
        self.operations = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
        self.data = [[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]]
        self.conjunction = [0, 0, 0, 1]
        self.disjunction = [0, 1, 1, 1]
        self.implication = [1, 1, 0, 1]
        self.exclusive = [0, 1, 1, 0]
        self.equivalence = [1, 0, 0, 1]

    def test_conjunction_equal(self):
        for i, data in enumerate(self.data):
            self.assertEqual(conjunction(data[0], data[1]), self.conjunction[i])

    def test_disjunction_equal(self):
        for i, data in enumerate(self.data):
            self.assertEqual(disjunction(data[0], data[1]), self.disjunction[i])

    def test_implication_equal(self):
        for i, data in enumerate(self.data):
            self.assertEqual(implication(data[0], data[1]), self.implication[i])

    def test_exclusive_equal(self):
        for i, data in enumerate(self.data):
            self.assertEqual(exclusive(data[0], data[1]), self.exclusive[i])

    def test_equivalence_equal(self):
        for i, data in enumerate(self.data):
            self.assertEqual(equivalence(data[0], data[1]), self.equivalence[i])
