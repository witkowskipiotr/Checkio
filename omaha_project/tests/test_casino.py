import unittest

from models.casino import Casino


class CasinoTest(unittest.TestCase):
    def setUp(self):
        # initialize person
        self.casino = Casino(name='Cristal Casino', adress='Królewska 11, Warszawa')

        # create 2 croupier
        self.gregor = self.casino.add_croupier(name='Grzegorz',
                                               surname='Brzęczyszczykiewicz',
                                               shuffle_last=True)
        self.pawel = self.casino.add_croupier(name='Paweł',
                                              surname='Dębowski',
                                              shuffle_last=False)

        # create players
        self.mike = self.casino.add_player(name='Michał', surname='Nowak',
                                           money=10, type='random')
        self.peter = self.casino.add_player(name='Piotr', surname='Witkowski',
                                            money=100.52, type='random')
        self.lukas = self.casino.add_player(name='Łukasz', surname='Witkowski',
                                            money=12, type='random')
        self.arthur = self.casino.add_player(name='Artur', surname='Witkowski',
                                             money=1000, type='random')

        # create table
        self.table_green = self.casino.add_table(name='Green')
        self.table_red = self.casino.add_table(name='Red')

    def test_check_players(self):
        # players join the table
        self.casino.add_player_to_table(name_table='Green', player=self.mike)
        self.casino.add_player_to_table(name_table='Green', player=self.lukas)
        self.casino.add_player_to_table(name_table='Green', player=self.arthur)

        self.game = self.casino.create_game_omaha(
            table_name='Green', money_min_to_connect=1, croupier=None)
        if self.game:
            # Croupier shuffle cards and get money from players
            self.game.start_game()

            # first step
            self.game.preflop_round()
            win = self.game.flop_round()
            if win and isinstance(win, bool):
                win = self.game.turn_round()
            if win and isinstance(win, bool):
                win = self.game.river_round()
            if win and isinstance(win, bool):
                win = self.game.check_winner()

            print(win.name)
            print(win.surname)

        print(self.casino.players)
        print(self.casino.croupier)

        # # create tree table
        # self.table_green = Table()
        # self.table_blue = Table()
        # self.table_red = Table()
        # # create two game by one table
        # self.green_omaha_one = self.table_green.start_the_game()
        # self.green_omaha_two = self.table_green.start_the_game()
