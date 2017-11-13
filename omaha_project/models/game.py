"""
Game Omaha Game
defined in https://en.wikipedia.org/wiki/Omaha_hold_%27em
"""
from models.deck import Deck
from models.table import Table
from models.people.croupier import Croupier


class Game:
    """
    Main class Table
    The dealer adds players and gives away cards
    """
    def __init__(self, *, table: Table, croupier: Croupier, game_players: list,
                 money_min_to_connect: float):
        self.deck = Deck()
        self.table = table
        self.croupier = croupier
        self.croupier.actual_table = self.table
        self.game_players = game_players
        self.money_min_to_connect = money_min_to_connect
        self.cards_on_table = []
        self.rate_of_the_game = 0
        self.step = 0
        self.amount_cards_on_table = 5

    def check_if_can_create_game(self) -> bool:
        """Check if you can create a game"""
        # if player have money then add to game
        for player in self.game_players:
            if player.check_money(money=self.money_min_to_connect) \
                    and player not in self.game_players:
                self.game_players.append(player)
        # if count of game players is less than 2 then game is not start
        if len(self.game_players) < 2:
            return False
        return True

    def start_game(self):
        """start the game"""
        self.croupier.shuffle_cards(deck=self.deck)
        for player in self.game_players:
            player.spend_money(money=self.money_min_to_connect)
            self.rate_of_the_game += self.money_min_to_connect

    def get_card(self):
        """Get card"""
        card = self.croupier.take_the_card_with_deck(deck=self.deck)
        return card

    def preflop_round(self):
        """
        1 step game
        Preflop Each player, receives four cards
        """
        for player in self.game_players:
            player.cards = []
            for number_of_cards in range(4):
                player.cards.append(self.get_card())
        self.step = 1

    def flop_round(self):
        """
        2 step game
        Flop Krupier puts on the table the first three common cards
        """
        self.cards_on_table.append(self.get_card())
        self.cards_on_table.append(self.get_card())
        self.cards_on_table.append(self.get_card())
        self.step = 2
        return self.check_win_before_end()

    def turn_round(self):
        """
        3 step game
        Turn on the table is the fourth common card
        """
        self.cards_on_table.append(self.get_card())
        self.step = 3
        return self.check_win_before_end()

    def river_round(self):
        """
        4 step game
        River The fifth and final common card is laid on the table.
        """
        self.cards_on_table.append(self.get_card())
        self.step = 4
        return self.check_win_before_end()

    def check_win_before_end(self):
        """
        Check that someone has not resigned from the game
        before the end of the game
        """
        for player in self.game_players:
            if player.when_finish_game == self.step:
                player.amount_lose += 1
                self.game_players.remove(player)

        if len(self.game_players) > 1:
            return True
        elif len(self.game_players) == 1:
            return self.game_players[0]
        return False

    def check_winner(self):
        """compares player cards"""
        pass
