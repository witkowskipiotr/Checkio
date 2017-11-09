"""
Game Omaha Game
defined in https://en.wikipedia.org/wiki/Omaha_hold_%27em
"""
import random


class Deck:
    """
    a class of playing cards
    """
    def __init__(self):
        self.colors = {'trefl': 1, '  pik': 2, ' karo': 3, ' kier': 4}
        self.numbers = {'2': 0, '3': 1, '4': 2, '5': 3,
                        '6': 4, '7': 5, '8': 6, '9': 7,
                        '10': 8, 'J': 9, 'Q': 10,
                        'K': 11, 'A': 12}
        self.get_new_shuffling_deck()

    def get_new_shuffling_deck(self):
        """
        when we start the game, we have to shuffing card
        """
        self.combination_of_cards = []
        for color in self.colors:
            for number in self.numbers:
                self.combination_of_cards.append(color + number)
        # Shuffling cards
        random.shuffle(self.combination_of_cards)

    def take_the_card_with_deck(self) -> list:
        """
        Takes one cardsdeck and passes it to the player
        Return: cardsto the player
        """
        if self.combination_of_cards:
            return self.combination_of_cards.pop()


class Player:
    """
    class of person player
    When person into the casino class is create, but he
    dies bit have join the game immediately (maybe he wants to drink first)
    """

    def __init__(self, *, name: str, surname: str, money: float):
        self.name = name
        self.surname = surname
        self.money = money
        self.cards = []
        self.game = []
        self.actual_table = None

    def log_in_table(self, *, table) -> bool:
        """If person return to the table where is login"""
        if self in table.person_at_the_table:
            self.actual_table = table
            return True

    def join_the_table(self, *, table):
        """One person can be only by one table"""
        if table._person_join_to_the_table(person=self):
            self.actual_table = table

    def out_the_table(self, *, table):
        """One person can be only by one table"""
        if self in table.person_at_the_table:
            table.person_at_the_table.remove(self)

    def join_the_game(self, game):
        """When person join game his cards is create"""

        self.game.append(game)
        self.cards = {1: '', 2: '', 3: '', 4: ''}

    def out_the_game(self):
        """When person aut of game his cards removed"""
        self.cards = []

    def person_add_money(self, *, money: float):
        """When person win money or get from bank, his wallet up"""
        self.money += round(money, 2)

    def spend_money(self, *, money: float):
        """when person buy drink or raises the stake by game"""
        self.money -= round(money, 2)


class Game(Deck):
    """
    Main class Table
    The dealer adds players and gives away cards
    """

    def __init__(self):
        self.amount_cards_on_table = 5
        super().__init__()
        self.players = []
        self.__rate_of_the_game = 0
        self.clean_card()
        self.max_amount_player = (len(self.combination_of_cards) - self.amount_cards_on_table) // 4

    def get_rate_of_the_game(self):
        """get velue by variable self.__rate_of_the_game"""
        return self.__rate_of_the_game

    def clean_card(self):
        """when we starts game game"""
        self.cards_on_table = {1: '', 2: '', 3: '', 4: '', 5: ''}

    def add_players(self, *, player: Player, money: float) -> bool:
        """add person to the game if is the required number of cards in the deck"""
        if player not in self.players and len(self.players) < self.max_amount_player:
            if player.money < money:
                return False
            else:
                player.spend_money(money=money)
                self.__rate_of_the_game += money

            self.players.append(player)
            # add player to list who play the game
            player.join_the_game(self)
            return True

    def remove_players_from_game(self, *, player: Player):
        """When person aut of game"""
        if player in self.players:
            self.players.remove(player)
            # remove player to list who play the game
            player.game.remove(player)

    def preflop_round(self):
        """
        1 step game
        Preflop Each player, receives four cards
        """
        for player in self.players:
            for card in player.cards:
                player.cards[card] = self.take_the_card_with_deck()

    def flop_round(self):
        """
        2 step game
        Flop Krupier puts on the table the first three common cards
        """
        self.cards_on_table[1] = self.take_the_card_with_deck()
        self.cards_on_table[2] = self.take_the_card_with_deck()
        self.cards_on_table[3] = self.take_the_card_with_deck()

    def turn_round(self):
        """
        3 step game
        Turn on the table is the fourth common card
        """
        self.cards_on_table[4] = self.take_the_card_with_deck()

    def river_round(self):
        """
        4 step game
        River The fifth and final common card is laid on the table.
        """
        self.cards_on_table[5] = self.take_the_card_with_deck()


class Table:
    """
    The table can be approached by many people, but at one table can be only two games.
    To play must be at the table.
    """
    def __init__(self):
        self.person_at_the_table = []
        self.max_game_on_the_table = 2
        self.game = []

    def start_the_game(self) -> Game:
        """initialize game"""
        if len(self.game) < self.max_game_on_the_table:
            game = Game()
            self.game.append(game)
            return game

    def stop_the_game(self, *, game: Game):
        """remove game from table"""
        return self.game.pop(game)

    def _person_join_to_the_table(self, *, person: Player) -> bool:
        """when the person approaches the table he is append to the table"""
        if person not in self.person_at_the_table:
            self.person_at_the_table.append(person)
            return True

    def _disconnect_person_by_table(self, *, person: Player):
        """when the person resigns from the table"""
        if person in self.person_at_the_table:
            self.person_at_the_table.remove(person)

    def perosn_join_to_the_game(self, *, person: Player, game: Game) -> bool:
        """If an existing person wants to join the game must be at the table."""
        if person in self.person_at_the_table and game in self.game:
            game.add_players(player=person)
            return True
