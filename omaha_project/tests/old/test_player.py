import unittest
from omaha import Player

class PersonTest(unittest.TestCase):

    def setUp(self):
        # initialize person
        self.gregor = Player(name='Grzegorz', surname='Brzęczyszczykiewicz', money=2.1)

    def test_add_person(self):
        anna = Player(name='Ania', surname='Morawska', money=3)
        self.assertEqual(anna.name, 'Ania')
        self.assertEqual(anna.surname, 'Morawska')
        self.assertEqual(anna.money, 3)
        self.assertFalse(anna.cards)

    def test_put_more_money(self):
        self.assertEqual(self.gregor.money, 2.1)
        self.gregor.person_add_money(money=0.1051111)
        self.assertEqual(self.gregor.money, 2.21)

    def test_spend_money(self):
        self.assertEqual(self.gregor.money, 2.1)
        self.gregor.spend_money(money=0.1)
        self.assertEqual(self.gregor.money, 2.0)