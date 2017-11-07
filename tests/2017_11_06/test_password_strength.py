import unittest

from code_2017_11_06.password_strength import validate_password


class CheckAnagramsWordTest(unittest.TestCase):

    # I. invalid password
    def test_only_number_password(self):
        self.assertFalse(validate_password(password='1234567890123456'))
        self.assertFalse(validate_password(password='123'))

    def test_only_upper_letter_password(self):
        self.assertFalse(validate_password(password='aaaaaaaaaaaaaaaaaaaaa'))
        self.assertFalse(validate_password(password='AAAbbbAAdsdSSdSAS'))
        self.assertFalse(validate_password(password='AbCdE'))

    def test_to_short_password(self):
        self.assertFalse(validate_password(password='Ab123'))
        self.assertFalse(validate_password(password='Ab3456789'))
        self.assertFalse(validate_password(password=''))

    # def test_characters_not_allowed_password(self):
    #     self.assertFalse(validate_password(password='IAKxnvZok,rsWP1S0NCfJq4pti9Q6c8gXm'))
    #     self.assertFalse(validate_password(password=' IAKxnvZokrsWP1S0NCfJq4pti9Q6c8gXm'))
    #     self.assertFalse(validate_password(password='IAKxnvZokrsWP1S0NCfJq4pti9Q6c8gXm,'))

    # II. valid password
    def test_valid_password(self):
        self.assertTrue(validate_password(password="AAbbcc1234"))
        self.assertTrue(validate_password(password="ULFFunH8ni"))
        self.assertTrue(validate_password(password="Uaaa21ADF1"))
