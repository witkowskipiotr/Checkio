import unittest

from elementary.checkio import fizz_buzz


class CheckioTest(unittest.TestCase):

    #FizzBuzz
    def test_fizz_buzz_invalid_number(self):
        self.assertRaises(TypeError, fizz_buzz, number='12')

    def test_fizz_buzz_not_equal(self):
        self.assertNotEqual(fizz_buzz(number=7), 'Fizz')
        self.assertNotEqual(fizz_buzz(number=15), 'Buzz')

    def test_fizz_buzz_equal(self):
        self.assertEqual(fizz_buzz(number=-2), '')
        self.assertEqual(fizz_buzz(number=7), '7')
        self.assertEqual(fizz_buzz(number=15), 'Fizz Buzz')
