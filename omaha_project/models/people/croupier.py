from models.people.person import Person
from models.deck import Deck
from random import shuffle


class Croupier(Person):
    """
    class Croupier, casino employee - leads the game
    """
    def __init__(self, *, name: str, surname: str, shuffle_last: bool):
        super().__init__(name=name, surname=surname)
        self.shuffle_last = shuffle_last
        self.actual_table = None

    def shuffle_cards(self, *, deck: Deck):
        """
        shuffles new cards to play
        """
        shuffle(deck.combination_of_cards)

    def take_the_card_with_deck(self, *, deck: Deck) -> str:
        """
        Takes one card with deck
        """
        if deck.combination_of_cards:
            if self.shuffle_last:
                return deck.combination_of_cards.pop()
            else:
                return deck.combination_of_cards.pop(0)

    def take_money_from_player(self, *, player, money):
        """
        Gets money for play from players
        """
        is_paid = player.spend_money(money=money)
        return is_paid
