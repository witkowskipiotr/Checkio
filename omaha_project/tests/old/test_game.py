import unittest

from models.Casino import Casino


class GameTest(unittest.TestCase):

    def setUp(self):
        # create casino


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

