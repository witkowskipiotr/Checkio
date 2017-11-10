import unittest
from omaha import Deck


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