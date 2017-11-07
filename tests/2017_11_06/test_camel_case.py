import unittest

from code_2017_11_06.camel_case import changelings_camel_case, to_camel_case


class CheckAnagramsWordTest(unittest.TestCase):

    def test_change_camel_case_with_one_sign(self):
        self.assertEqual(changelings_camel_case(text='the_stealth_warrior', sign='_'), 'theStealthWarrior')
        self.assertEqual(changelings_camel_case(text='The-Stealth-Warrior', sign='-'), 'TheStealthWarrior')
        self.assertEqual(changelings_camel_case(text='A-B-C', sign='-'), 'ABC')

    def test_not_change_camel_case_with_one_sign(self):
        self.assertEqual(changelings_camel_case(text='the_stealth_warrior', sign='-'), 'the_stealth_warrior')
        self.assertEqual(changelings_camel_case(text='The-Stealth-Warrior', sign='_'), 'The-Stealth-Warrior')
        self.assertEqual(changelings_camel_case(text='A-B-C', sign='_'), 'A-B-C')

    def test_main_function_convert_two_sign(self):
        self.assertEqual(to_camel_case(text='The-cat_was-evil'), 'TheCatWasEvil')
        self.assertEqual(to_camel_case(text='the_pippi-is_cute'), 'thePippiIsCute')
        self.assertEqual(to_camel_case(text='a_cat_is-cute'), 'aCatIsCute')
        self.assertEqual(to_camel_case(text='the_Cat-was-Omoshiroi'), 'theCatWasOmoshiroi')
        self.assertEqual(to_camel_case(text='a-pippi_Is_Savage'), 'aPippiIsSavage')
        self.assertEqual(to_camel_case(text='A_cat_Is_Savage'), 'ACatIsSavage')
        self.assertEqual(to_camel_case(text='the_cat-Was_Savage'), 'theCatWasSavage')
