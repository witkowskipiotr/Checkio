import unittest

from models.game import Game
from models.game import Deck
from models.casino import Casino


class GameTest(unittest.TestCase):

    def create_game(self, *, name: str, money_min_to_connect: float, game_players: list) -> Game:
        if name not in self.casino.tables:
            return None

        self.game = Game(table=self.casino.tables[name], croupier=self.croupier,
                         money_min_to_connect=money_min_to_connect,
                         game_players=game_players)
        return self.game

    def setUp(self):
        # initialize person
        self.casino = Casino(name='Cristal Casino', adress='Królewska 11, Warszawa')
        self.casino.add_table(name='Green', max_number_of_players=4)
        # create croupier
        self.croupier = self.casino.add_croupier(name='Grzegorz',
                                                 surname='Brzęczyszczykiewicz',
                                                 shuffle_last=True)
        # create players
        self.mike = self.casino.add_player(name='Michał', surname='Nowak',
                                           money=10, type_player='normal')
        self.peter = self.casino.add_player(name='Piotr', surname='Witkowski',
                                            money=100.52, type_player='normal')
        # add player to the table
        self.casino.add_player_to_table(name_table='Green', player=self.mike)
        self.casino.add_player_to_table(name_table='Green', player=self.peter)
        # start game
        self.game = self.create_game(name='Green', money_min_to_connect=5,
                                     game_players=[self.mike, self.peter])

    def test_new_game(self):
        self.assertEqual(self.game.table, self.casino.tables['Green'])
        self.assertEqual(self.game.croupier, self.croupier)
        self.assertEqual(self.game.croupier.actual_table, self.game.table)
        self.assertEqual(self.game.money_min_to_connect, 5)
        self.assertEqual(self.game.rate_of_the_game, 0)
        self.assertEqual(self.game.step, 0)
        self.assertEqual(self.game.cards_on_table, [])
        self.assertIn(self.mike, self.game.game_players)
        self.assertIn(self.peter, self.game.game_players)

    def test_check_can_create_game(self):
        # not table in casino
        self.game_new = self.create_game(name='Red', money_min_to_connect=5,
                                         game_players=[self.mike, self.peter])
        self.assertFalse(self.game_new)

        # add table
        self.casino.add_table(name='Red', max_number_of_players=5)

        self.game = Game(table=self.casino.tables['Red'], croupier=self.croupier,
                         money_min_to_connect=3,
                         game_players=[self.mike])

        # To low players - 1 player - cant create game
        self.assertFalse(self.game.check_if_can_create_game())
        self.game.game_players.append(self.peter)
        # We can start game
        self.assertTrue(self.game.check_if_can_create_game())

    def test_start_game(self):
        # table green can create game
        self.assertTrue(self.game.check_if_can_create_game())
        # create new deck
        deck_new = Deck()
        self.assertEqual(self.game.deck.combination_of_cards, deck_new.combination_of_cards)
        # check money Mike
        self.assertEqual(self.mike.money, 10)
        self.game.start_game()
        # not equal because shuffle card
        self.assertNotEqual(self.game.deck.combination_of_cards, deck_new.combination_of_cards)
        # because game take 5 PLN by mike
        self.assertEqual(self.mike.money, 5)
        # take money by peter and mike
        self.assertEqual(self.game.rate_of_the_game, 10)

    def test_get_card(self):
        deck_new = Deck()
        self.game.start_game()
        # 52 count of cards
        self.assertEqual(len(self.game.deck.combination_of_cards), 52)
        card = self.game.get_card()
        # take 1 -> 52 - 1 = 51
        self.assertEqual(len(self.game.deck.combination_of_cards), 51)
        # exists element by new deck
        self.assertIn(card, deck_new.combination_of_cards)
        # not exists element by this deck
        self.assertNotIn(card, self.game.deck.combination_of_cards)

    def test_preflop_round(self):
        self.game.start_game()
        self.assertEqual(self.game.step, 0)
        self.game.preflop_round()
        # 4 card for 2 players -> 52 - 4 * 2 = 44
        self.assertEqual(len(self.game.deck.combination_of_cards), 44)
        self.assertEqual(self.game.step, 1)
        self.assertFalse(self.game.cards_on_table)

    def test_flop_round(self):
        self.game.start_game()
        self.game.preflop_round()
        self.game.flop_round()
        # 3 card for tables -> 44 - 3 = 41
        self.assertEqual(len(self.game.deck.combination_of_cards), 41)
        self.assertEqual(self.game.step, 2)
        self.assertEqual(len(self.game.cards_on_table), 3)

    def test_turn_round(self):
        self.game.start_game()
        self.game.preflop_round()
        self.game.flop_round()
        self.game.turn_round()
        # 1 card for tables -> 41 - 1 = 40
        self.assertEqual(len(self.game.deck.combination_of_cards), 40)
        self.assertEqual(self.game.step, 3)
        self.assertEqual(len(self.game.cards_on_table), 4)

    def test_river_round(self):
        self.game.start_game()
        self.game.preflop_round()
        self.game.flop_round()
        self.game.turn_round()
        self.game.river_round()
        # 1 card for tables -> 40 - 1 = 39
        self.assertEqual(len(self.game.deck.combination_of_cards), 39)
        self.assertEqual(self.game.step, 4)
        self.assertEqual(len(self.game.cards_on_table), 5)

    def test_check_win_before_end(self):
        # peter and mike are normal players and they not pass game
        self.game.start_game()
        self.game.preflop_round()
        self.game.flop_round()
        self.assertEqual(self.game.check_win_before_end(), True)
        self.game.turn_round()
        # change peter pass game by step 3
        self.peter.when_finish_game = 3
        # mike winn before end
        self.assertEqual(self.game.check_win_before_end(), self.mike)

    def test_check_win_before_end_second(self):
        # players join the table
        self.casino.add_player_to_table(name_table='Green', player=self.mike)
        self.casino.add_player_to_table(name_table='Green', player=self.peter)

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
            if win and not isinstance(win, bool):
                print(win.name)
                print(win.surname)
