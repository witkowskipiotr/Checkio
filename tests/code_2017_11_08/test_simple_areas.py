import unittest

from code_2017_11_08.simple_areas import simple_areas 


class SimpleAreasTest(unittest.TestCase):

    def test_circle_areas(self):
        self.assertEqual(simple_areas(3), 7.07)
        self.assertEqual(simple_areas(1.34), 1.41)

    def test_rectangle_areas(self):
        self.assertEqual(simple_areas(2, 2), 4)
        self.assertEqual(simple_areas(2, 3), 6)

    def test_triangle_areas(self):
        self.assertEqual(simple_areas(3, 5, 4), 6)
        self.assertEqual(simple_areas(1.5, 2.5, 2), 1.5)
