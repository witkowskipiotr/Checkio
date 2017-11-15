import unittest

from models.casino import Casino


class CasinoTest(unittest.TestCase):

    def add_cassino(self):
        self.casino_new = Casino(name='Royal Casino', adress='Warszawska 1, Warszawa')

    def setUp(self):
        # initialize casino
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
                                           money=10, type_player='random')
        self.peter = self.casino.add_player(name='Piotr', surname='Witkowski',
                                            money=100.52, type_player='random')
        self.lukas = self.casino.add_player(name='Łukasz', surname='Witkowski',
                                            money=12, type_player='random')
        self.arthur = self.casino.add_player(name='Artur', surname='Witkowski',
                                             money=1000, type_player='random')

        # create table
        self.table_green = self.casino.add_table(name='Green', max_number_of_players=3)
        self.table_red = self.casino.add_table(name='Red', max_number_of_players=4)

    def test_new_casino(self):
        self.add_cassino()
        self.assertEqual(self.casino_new.name, 'Royal Casino')
        self.assertEqual(self.casino_new.adress, 'Warszawska 1, Warszawa')
        self.assertFalse(self.casino_new.croupier)
        self.assertFalse(self.casino_new.players)
        self.assertFalse(self.casino_new.tables)

    def test_add_del_croupier(self):
        self.add_cassino()
        self.assertFalse(self.casino_new.croupier)
        # add croupier
        self.mario = self.casino_new.add_croupier(name="Mariusz",
                                                  surname="Wlazły",
                                                  shuffle_last=False)
        self.assertIn(self.mario, self.casino_new.croupier)
        # dell croupier in casino
        self.casino_new.del_croupier(self.mario)
        self.assertFalse(self.casino_new.croupier)

    def test_get_default_croupier(self):
        # get croupier from available
        croupier = self.casino.get_default_croupier()
        self.assertIn(croupier, self.casino.croupier)

        # start game and get one croupier - 1 available croupier
        self.casino.add_player_to_table(name_table='Green', player=self.arthur)
        self.casino.add_player_to_table(name_table='Green', player=self.lukas)
        self.game = self.casino.create_game_omaha(table_name='Green',
                                                      croupier=self.gregor,
                                                      money_min_to_connect=3)
        self.game.start_game()
        # croupier gregor is in the game and available crupier is pawel
        self.assertEqual(self.pawel, self.casino.get_default_croupier())
        # check 2 time from true
        self.assertEqual(self.pawel, self.casino.get_default_croupier())
        # stil 2 croupier in casino
        self.assertEqual(len(self.casino.croupier), 2)

    def test_add_del_player(self):
        cout_player = len(self.casino.players)
        # add player
        self.lily = self.casino.add_player(name='Lily', surname='Potter',
                                           money=200, type_player='random')
        cout_player_after_append = len(self.casino.players)
        self.assertEqual(cout_player, cout_player_after_append - 1)
        self.assertIn(self.lily, self.casino.players)
        # del player
        self.casino.del_player(self.lily)
        cout_player_after_dell = len(self.casino.players)
        self.assertEqual(cout_player, cout_player_after_dell)
        self.assertNotIn(self.lily, self.casino.players)

    def test_add_del_table(self):
        self.assertIn('Red', self.casino.tables)
        self.casino.del_table(name='Red')
        self.assertNotIn('Red', self.casino.tables)

    def test_add_del_player_table(self):
        self.assertEqual(len(self.casino.tables['Red'].person_at_the_table), 0)
        # add player to table
        self.casino.add_player_to_table(name_table='Red', player=self.lukas)
        self.assertIn(self.lukas, self.casino.tables['Red'].person_at_the_table)
        self.assertEqual(len(self.casino.tables['Red'].person_at_the_table), 1)
        self.assertEqual(self.lukas.actual_table, self.casino.tables['Red'])
        # del player from table
        self.casino.del_player_from_table(name_table='Red', player=self.lukas)
        self.assertNotIn(self.lukas, self.casino.tables['Red'].person_at_the_table)
        self.assertEqual(self.lukas.actual_table, None)

    def test_check_if_can_create_game(self):
        # table not exists
        self.assertEqual(
            self.casino.check_if_can_create_game(table_name='Grey', croupier=self.gregor,
                                                 money_min_to_connect=1), (None, None))
        # nobody is in the table - min 2 player
        self.assertEqual(
            self.casino.check_if_can_create_game(table_name='Green', croupier=self.gregor,
                                                 money_min_to_connect=1), (None, None))
        self.casino.add_player_to_table(name_table='Green', player=self.peter)
        self.casino.add_player_to_table(name_table='Green', player=self.lukas)
        # we set mike to croupier, but he is not croupier and get available croupier
        # game start
        self.assertTrue(
            self.casino.check_if_can_create_game(table_name='Green', croupier=self.mike,
                                                 money_min_to_connect=1) != (None, None))

    def test_create_game_omaha(self):
        # Not Join players this we checki in test_check_if_can_create_game
        game = self.casino.create_game_omaha(table_name='Green', croupier=self.gregor,
                                             money_min_to_connect=3)
        self.assertEqual(game, None)

        # add player
        self.casino.add_player_to_table(name_table='Green', player=self.mike)
        self.casino.add_player_to_table(name_table='Green', player=self.arthur)
        # game create
        game = self.casino.create_game_omaha(table_name='Green', croupier=self.gregor,
                                             money_min_to_connect=3)
        self.assertNotEqual(game, None)

    def test_cant_create_game_by_table(self):
        # create table
        self.table_green = self.casino.add_table(name='Yellow', max_number_of_players=1)
        # add player
        self.casino.add_player_to_table(name_table='Yellow', player=self.mike)
        # dont add player because max_number_of_players is only 1, we cant start game witch 1 players
        self.casino.add_player_to_table(name_table='Yellow', player=self.arthur)

        game = self.casino.create_game_omaha(table_name='Yellow', croupier=self.gregor,
                                             money_min_to_connect=1)
        self.assertEqual(game, None)
