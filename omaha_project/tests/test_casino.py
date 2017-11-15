import unittest

from models.casino import Casino


class CasinoTest(unittest.TestCase):

    def initialize_full_item(self):
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
        self.casino = Casino(name='Royal Casino', adress='Warszawska 1, Warszawa')
        self.assertEqual(self.casino.name, 'Royal Casino')
        self.assertEqual(self.casino.adress, 'Warszawska 1, Warszawa')
        self.assertFalse(self.casino.croupier)
        self.assertFalse(self.casino.players)
        self.assertFalse(self.casino.tables)

    def test_add_del_croupier(self):
        self.casino = Casino(name='Royal Casino', adress='Warszawska 1, Warszawa')
        self.assertFalse(self.casino.croupier)
        # add croupier
        self.mario = self.casino.add_croupier(name="Mariusz",
                                                  surname="Wlazły",
                                                  shuffle_last=False)
        self.assertIn(self.mario, self.casino.croupier)
        # dell croupier in casino
        self.casino.del_croupier(self.mario)
        self.assertFalse(self.casino.croupier)

    def test_get_default_croupier(self):
        self.initialize_full_item()
        # get croupier from available
        croupier = self.casino.get_default_croupier()
        self.assertIn(croupier, self.casino.croupier)

    def test_get_default_croupier_when_one_is_busy(self):
        self.initialize_full_item()
        # add players to the table
        self.casino.add_player_to_table(name_table='Green', player=self.arthur)
        self.casino.add_player_to_table(name_table='Green', player=self.lukas)
        # start game and get one croupier - 1 available croupier
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

    def test_add_player(self):
        self.initialize_full_item()
        cout_player = len(self.casino.players)
        # add player
        self.lily = self.casino.add_player(name='Lily', surname='Potter',
                                           money=200, type_player='random')
        cout_player_after_append = len(self.casino.players)
        self.assertEqual(cout_player, cout_player_after_append - 1)
        self.assertIn(self.lily, self.casino.players)

    def test_del_player(self):
        self.initialize_full_item()
        self.lily = self.casino.add_player(name='Lily', surname='Potter',
                                           money=200, type_player='random')
        # del player
        self.casino.del_player(self.lily)
        self.assertNotIn(self.lily, self.casino.players)

    def test_add_table(self):
        self.initialize_full_item()
        self.assertNotIn('Pink', self.casino.tables)
        self.casino.add_table(name='Pink', max_number_of_players=4)
        self.assertIn('Pink', self.casino.tables)

    def test_del_table(self):
        self.initialize_full_item()
        self.assertIn('Red', self.casino.tables)
        self.casino.del_table(name='Red')
        self.assertNotIn('Red', self.casino.tables)

    def test_add_player_table(self):
        self.initialize_full_item()
        self.assertEqual(len(self.casino.tables['Red'].person_at_the_table), 0)
        # add player to table
        self.casino.add_player_to_table(name_table='Red', player=self.lukas)
        self.assertIn(self.lukas, self.casino.tables['Red'].person_at_the_table)
        self.assertEqual(len(self.casino.tables['Red'].person_at_the_table), 1)
        self.assertEqual(self.lukas.actual_table, self.casino.tables['Red'])

    def test_del_player_table(self):
        self.initialize_full_item()
        # add player to table
        self.casino.add_player_to_table(name_table='Red', player=self.lukas)
        # del player from table
        self.casino.del_player_from_table(name_table='Red', player=self.lukas)
        self.assertNotIn(self.lukas, self.casino.tables['Red'].person_at_the_table)
        self.assertEqual(self.lukas.actual_table, None)

    def test_cant_create_game_when_not_table(self):
        self.initialize_full_item()
        # table not exists
        self.assertEqual(
            self.casino.check_if_can_create_game(table_name='Grey', croupier=self.gregor,
                                                 money_min_to_connect=1), (None, None))

    def test_cant_create_game_when_to_small_players(self):
        self.initialize_full_item()
        # nobody is in the table - min 2 player
        self.assertEqual(
            self.casino.check_if_can_create_game(table_name='Green', croupier=self.gregor,
                                                 money_min_to_connect=1), (None, None))

    def test_can_create_game(self):
        self.initialize_full_item()
        self.casino.add_player_to_table(name_table='Green', player=self.peter)
        self.casino.add_player_to_table(name_table='Green', player=self.lukas)
        # we set mike to croupier, but he is not croupier and get available croupier
        # game start
        self.assertTrue(
            self.casino.check_if_can_create_game(table_name='Green', croupier=self.mike,
                                                 money_min_to_connect=1) != (None, None))

    def test_cont_create_game_omaha_small_players(self):
        self.initialize_full_item()
        # Not Join players this we check in test_check_if_can_create_game
        game = self.casino.create_game_omaha(table_name='Green', croupier=self.gregor,
                                             money_min_to_connect=3)
        self.assertEqual(game, None)

    def test_cant_create_game_omaha_small_number_max_player_by_table(self):
        self.initialize_full_item()
        # create table
        self.table_green = self.casino.add_table(name='Yellow', max_number_of_players=1)
        # add player
        self.casino.add_player_to_table(name_table='Yellow', player=self.mike)
        # don`t add player because max_number_of_players is only 1, we cant start game witch 1 players
        self.casino.add_player_to_table(name_table='Yellow', player=self.arthur)

        game = self.casino.create_game_omaha(table_name='Yellow', croupier=self.gregor,
                                             money_min_to_connect=1)
        self.assertEqual(game, None)

    def test_can_create_game_omaha(self):
        self.initialize_full_item()
        # add player
        self.casino.add_player_to_table(name_table='Green', player=self.mike)
        self.casino.add_player_to_table(name_table='Green', player=self.arthur)
        # game create
        game = self.casino.create_game_omaha(table_name='Green', croupier=self.gregor,
                                             money_min_to_connect=3)
        self.assertTrue(game)