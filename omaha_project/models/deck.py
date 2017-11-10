class Deck:
    """
    a class of playing cards
    """
    def __init__(self):

        self.combination_of_cards = []
        self.colors = {'trefl': 1, '  pik': 2, ' karo': 3, ' kier': 4}
        self.numbers = {'2': 0, '3': 1, '4': 2, '5': 3,
                        '6': 4, '7': 5, '8': 6, '9': 7,
                        '10': 8, 'J': 9, 'Q': 10,
                        'K': 11, 'A': 12}
        self.get_new_deck()

    def get_new_deck(self):
        """
        new deck
        """
        for color in self.colors:
            for number in self.numbers:
                self.combination_of_cards.append(color + number)
