import unittest

from home.house_password import house_password


class CheckioTest(unittest.TestCase):

    def test_house_password_not_equal(self):
        self.assertNotEqual(house_password("b"), True)

    def test_house_password_equal(self):
        # first argument is a text, second is solution
        self.values = [
            ('A1213pokl', False),
            ('bAse730onE', True),
            ('asasasasasasasaas', False),
            ('QWERTYqwerty', False),
            ('123456123456', False),
            ('QwErTy911poqqqq', True),
        ]
        for value in self.values:
            self.assertEqual(house_password(value[0]),value[1])
