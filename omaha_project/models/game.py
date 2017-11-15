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
        self.hierarchy = {'Royal flush': 1, 'Straight flush': 2, 'Quads': 3,
                     'Full': 4, 'Flush': 5, 'Straight': 6, 'Three': 7,
                     'Two Pairs': 8, 'A Pair': 9, 'None': 20}

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





    def cards_split(self, *, cards: list) -> list:
        result = [(card[:5], card[5:]) for card in cards]
        return result

    def get_count_card(self, *, cards_number: list) -> list:
        count_card = set()
        for card in cards_number:
            if cards_number.count(card) > 1:
                count_card.add((cards_number.count(card), card))
        result = list(count_card)
        sorted(result, key=lambda cards: cards[0])
        return result

    def amount_consecutive_items(self, *, cards_number: list) -> tuple:
        card_old = None
        for item, card in enumerate(cards_number):
            if not card_old:
                card_old = card
            elif card_old != card:
                card_old += 1
                break
            card_old += 1
        return (item + 1, card_old - 1)

    def check_card_layout(self, *, cards: list) -> (str, list):
        result = ''
        cards = self.cards_split(cards=cards)
        cards_colour = sorted([self.deck.colors[card[0]] for card in cards])
        cards_number = sorted([self.deck.numbers[card[1]] for card in cards])

        # check flush
        is_flush = all(card == cards_colour[0] for card in cards_colour)

        # check_straight
        amount, card_straight = self.amount_consecutive_items(cards_number=cards_number)
        is_straight = amount == 5

        # check 'Royal flush', 'Straight flush', 'Flush', 'Straight'
        if is_flush and is_straight and card_straight == self.deck.numbers['A']:
            return 'Royal flush', [card_straight]
        elif is_flush and is_straight:
            return 'Straight flush', [[card_straight]]
        elif is_flush:
            return 'Flush', [cards_number]
        elif is_straight:
            return 'Straight', [cards_number]

        # get count repeated cards
        amount_item = self.get_count_card(cards_number=cards_number)

        # check if it is two pair or full
        if len(amount_item) > 1:
            if amount_item[0][0] == 3:
                return 'Full', amount_item
            return 'Two Pairs', amount_item

        # check if it is quads, three or a pair
        if len(amount_item) == 1:
            if amount_item[0][0] == 4:
                return 'Quads', amount_item
            elif amount_item[0][0] == 3:
                return 'Three', amount_item
            elif amount_item[0][0] == 2:
                return 'A Pair', amount_item
        return 'None', []

    def best_combination_card_layout(self, *, player):
        cards = self.cards_split(cards=player.cards)
        cards_number_player = [self.deck.numbers[card[1]] for card in cards]
        sorted(cards_number_player)
        best_layout = ('None', cards_number_player)
        for index_cards_table in range(len((self.cards_on_table))-1):
            cards_table = self.cards_on_table[index_cards_table : index_cards_table + 3]
            for index_cards_player in range(len((player.cards)) - 1):
                cards_player = player.cards[index_cards_player: index_cards_player + 2]

                result = self.check_card_layout(cards=cards_table+cards_player)
                if result[0] and self.hierarchy[result[0]] < self.hierarchy[best_layout[0]]:
                    best_layout = result
        return best_layout

    def who_win(self):
        """compares player cards"""
        list_result = []
        for player in self.game_players:
            result = self.best_combination_card_layout(player=player)
            list_result.append([self.hierarchy[result[0]], result, player])
        sorted(list_result, key=lambda item: list_result[0])

        self.list_best = [best for best in list_result if best[0] == list_result[0][0]]

        if len(self.list_best) == 1:
            # return player
            return list_result[0][2]
        elif len(self.list_best) > 1:
            # take to compare
            winner = self.compare_result()

            return self.list_best[0]
        return self.game_players[0]

    def compare_result(self):
        take_result = list()
        method_result = ''
        for player_result in self.list_best:
            # method compare 1. color, 2. card
            colour = player_result[1][1][0][0]
            if player_result[1][0] == 'Straight flush':
                method_result = 'number'
                take_result.append([colour, player_result[2]])

            if player_result[1][0] == 'Flush':
                method_result = 'color'
                take_result.append([colour, player_result[2]])

        if method_result == 'number':
            a = sorted(take_result, key=lambda number: number[0])
            a = sorted(take_result, key=lambda number: number[0], reverse=True)
            return take_result[0][1]

        if method_result == 'color':
            sorted(take_result, key=lambda colour: take_result[0], reverse=True)
            return take_result[0][1]





        self.hierarchy = {'Royal flush': 1, 'Straight flush': 2, 'Quads': 3,
                     'Full': 4, 'Flush': 5, 'Straight': 6, 'Three': 7,
                     'Two Pairs': 8, 'A Pair': 9, 'None': 20}