import unittest

from omaha.omaha import *


class DeckTest(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.cards= ''
        self.cards_in_deck = len(self.deck.colors) * len(self.deck.numbers)
        self.border_between_index_colour_and_number = 5

    def test_get_some_card(self):
        # check than amount of cards in deck is equal amount of combination of cards
        self.assertTrue(len(self.deck.combination_of_cards) == self.cards_in_deck)
        # take a card
        self.cards= self.deck.take_the_card_with_deck()
        # check than cardsis no empty
        self.assertTrue(self.cards!= '')
        # check than amount of available cards is tru
        self.assertTrue(len(self.deck.combination_of_cards) == self.cards_in_deck - 1)
        # check than cardsis in colors on the deck
        self.assertTrue(self.cards[:self.border_between_index_colour_and_number] in self.deck.colors)
        # check than cardsis in numbers on the deck
        self.assertTrue(self.cards[self.border_between_index_colour_and_number:] in self.deck.numbers)

    def test_take_every_card_in_deck(self):
        for index in range(self.cards_in_deck):
            self.cards= self.deck.take_the_card_with_deck()
            self.assertTrue(self.cards)

    def test_take_no_exist_card(self):
        self.test_take_every_card_in_deck()
        self.cards= self.deck.take_the_card_with_deck()
        self.assertEqual(self.cards, None)


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


class TableTest(unittest.TestCase):

    def setUp(self):
        # initialize person
        self.gregor = Player(name='Grzegorz', surname='Brzęczyszczykiewicz', money=0)
        self.mike = Player(name='Michał', surname='Nowak', money=10)
        self.peter = Player(name='Piotr', surname='Witkowski', money=100)
        self.lukas = Player(name='Łukasz', surname='Witkowski', money=100)
        self.arthur = Player(name='Artur', surname='Witkowski', money=100)
        # create tree table
        self.table_green = Table()
        self.table_blue = Table()
        self.table_red = Table()
        # create two game by one table
        self.green_omaha_one = self.table_green.start_the_game()
        self.green_omaha_two = self.table_green.start_the_game()

    def test_person_join_table(self):
        self.peter.join_the_table(table=self.table_green)

        # check than peter is by table green
        self.assertTrue(self.peter.actual_table)
        self.assertTrue(self.peter.actual_table == self.table_green)

        # check than by table is peter
        self.assertIn(self.peter, self.table_green.person_at_the_table, "Peter is not by the table")

    def test_person_not_in_table(self):
        self.assertNotEqual(self.peter.actual_table, self.table_green)
        self.assertNotIn(self.peter, self.table_green.person_at_the_table)
        self.peter.join_the_table(table=self.table_red)
        self.assertNotEqual(self.peter.actual_table, self.table_green)
        self.assertNotIn(self.peter, self.table_green.person_at_the_table)

    def test_person_is_in_table(self):
        self.assertNotEqual(self.peter.actual_table, self.table_green)
        self.assertNotIn(self.peter, self.table_green.person_at_the_table)
        self.peter.join_the_table(table=self.table_green)
        self.assertEqual(self.peter.actual_table, self.table_green)
        self.assertIn(self.peter, self.table_green.person_at_the_table)

    def test_persons_is_in_table_and_migrate_table(self):
        self.peter.join_the_table(table=self.table_green)
        self.mike.join_the_table(table=self.table_green)
        self.gregor.join_the_table(table=self.table_green)
        self.lukas.join_the_table(table=self.table_green)
        self.arthur.join_the_table(table=self.table_green)
        self.arthur.join_the_table(table=self.table_red)

        # check than person is by the table
        self.assertIn(self.peter, self.table_green.person_at_the_table)
        self.assertIn(self.mike, self.table_green.person_at_the_table)
        self.assertIn(self.gregor, self.table_green.person_at_the_table)
        self.assertIn(self.lukas, self.table_green.person_at_the_table)
        self.assertIn(self.arthur, self.table_green.person_at_the_table)
        self.assertIn(self.arthur, self.table_red.person_at_the_table)

        # check than person is actual by table
        self.assertEqual(self.peter.actual_table, self.table_green)
        self.assertEqual(self.mike.actual_table, self.table_green)
        self.assertEqual(self.gregor.actual_table, self.table_green)
        self.assertEqual(self.lukas.actual_table, self.table_green)
        self.assertEqual(self.arthur.actual_table, self.table_red)

        # arthur is by the table_red and table_gree, but actual is only by table red
        self.assertNotEqual(self.arthur.actual_table, self.table_green)

        # arthur go to table_green
        self.arthur.log_in_table(table=self.table_green)
        self.assertNotEqual(self.arthur.actual_table, self.table_red)
        self.assertEqual(self.arthur.actual_table, self.table_green)
        self.assertIn(self.arthur, self.table_green.person_at_the_table)
        self.assertIn(self.arthur, self.table_red.person_at_the_table)


class GameTest(unittest.TestCase):

    def setUp(self):
        # initialize person
        self.gregor = Player(name='Grzegorz', surname='Brzęczyszczykiewicz', money=0)
        self.mike = Player(name='Michał', surname='Nowak', money=10)
        self.peter = Player(name='Piotr', surname='Witkowski', money=100)
        self.lukas = Player(name='Łukasz', surname='Witkowski', money=100)
        self.arthur = Player(name='Artur', surname='Witkowski', money=100)
        # create tree table
        self.table_green = Table()
        self.table_blue = Table()
        self.table_red = Table()
        # create two game by one table
        self.green_omaha_one = self.table_green.start_the_game()
        self.green_omaha_two = self.table_green.start_the_game()

    def test_game_omaha(self):
        # person join to the table
        self.peter.join_the_table(table=self.table_green)
        self.mike.join_the_table(table=self.table_green)
        self.gregor.join_the_table(table=self.table_green)
        self.lukas.join_the_table(table=self.table_green)
        self.arthur.join_the_table(table=self.table_green)

        # peter, mike, arthur join the game self.green_omaha_one
        self.green_omaha_one.add_players(player=self.peter, money=1)
        self.green_omaha_one.add_players(player=self.mike, money=1)
        self.green_omaha_one.add_players(player=self.arthur, money=1)
        # 1 step game
        self.green_omaha_one.preflop_round()
        # check game cards players
        print('peter', self.peter.cards)
        print('mike', self.mike.cards)
        print('arthur', self.arthur.cards)

        # check rate of the game
        print('Rate of the game is:', self.green_omaha_one.get_rate_of_the_game(), 'PLN')
        self.assertEqual(self.green_omaha_one.get_rate_of_the_game(), 3)

        # 2 step game
        self.green_omaha_one.flop_round()
        # check card on the table
        print('table 2 step', self.green_omaha_one.cards_on_table)

        # 3 step game
        self.green_omaha_one.turn_round()
        # check card on the table
        print('table 3', self.green_omaha_one.cards_on_table)

        # 4 step game
        self.green_omaha_one.river_round()
        # check card on the table
        print('table 4', self.green_omaha_one.cards_on_table)

