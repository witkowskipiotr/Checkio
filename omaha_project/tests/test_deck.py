import unittest

from models.deck import Deck


class DeckTest(unittest.TestCase):
    def test_colour_in_new_deck(self):
        deck = Deck()
        deck.get_new_deck()
        self.assertIn('trefl', deck.colors)
        self.assertIn('  pik', deck.colors)
        self.assertIn(' karo', deck.colors)

    def test_number_in_new_deck(self):
        deck = Deck()
        deck.get_new_deck()
        self.assertIn('2', deck.numbers)
        self.assertIn('7', deck.numbers)
        self.assertIn('A', deck.numbers)

    def test_combination_of_cards_in_new_deck(self):
        deck = Deck()
        deck.get_new_deck()
        self.assertIn(' kierJ', deck.combination_of_cards)
        self.assertIn(' karo2', deck.combination_of_cards)
        self.assertIn('  pikA', deck.combination_of_cards)
        self.assertIn('trefl10', deck.combination_of_cards)
