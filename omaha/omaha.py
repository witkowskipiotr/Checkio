import random

CARDS_ON_TABLE = 5
COLORS = {'trefl': 1, '  pik': 2, ' karo': 3, ' kier': 4}
NUMBERS = {'2': 0, '3': 1, '4': 2, '5': 3,
           '6': 4, '7': 5, '8': 6, '9': 7,
           '10': 8, 'J': 9, 'Q': 10,
           'K': 11, 'A': 12}


class Deck:
    """
    a class of playing cards
    """
    def __init__(self):
        self.get_new_shuffling_deck()

    def get_new_shuffling_deck(self):
        """
        when we start the game, we have to shuffing card
        """
        self.combination_of_cards = list()
        for color in COLORS:
            for number in NUMBERS:
                self.combination_of_cards.append(color+number)
        # Shuffling cards
        random.shuffle(self.combination_of_cards)

    def take_the_card_with_deck(self):
        """
        Takes one card deck and passes it to the player
        Return: card to the player
        """
        if self.combination_of_cards:
            return self.combination_of_cards.pop()


class Player:
    """
    class of person player
    When person into the casino class is create, but he
    dies bit have join the game immediately (maybe he wants to drink first)
    """
    def __init__(self, name, surname, money):
        self.name = name
        self.surname = surname
        self.money = money

    def join_the_table(self, table):
        self.join_the_game()
        table.join_to_the_table(self)

    def join_the_game(self):
        self.card = {1: '', 2: '', 3: '', 4: ''}

    def putting_money(self, money):
        self.money += money


class Game(Deck):
    """
    Main class Table
    The dealer adds players and gives away cards
    """
    def __init__(self):
        super().__init__()
        self.players = []
        self.clean_card()
        self.max_amount_player = (len(self.combination_of_cards) - CARDS_ON_TABLE) // 4

    def clean_card(self):
        self.card = {1: '', 2: '', 3: '', 4: '', 5: ''}

    def add_players(self, player):
        if player not in self.players and len(self.players) < self.max_amount_player:
            self.players.append(player)
            return True

    def distribute_cards_to_players(self):
        # Giving cards to players
        for player in self.players:
            for card in player.card:
                player.card[card] = self.take_the_card_with_deck()

        # Giving cards to the table
        for card in self.card:
            self.card[card] = self.take_the_card_with_deck()


class Table:
    def __init__(self):
        self.person_at_the_table = []
        self.max_game_on_the_table = 2
        self.game = []

    def start_the_game(self):
        if len(self.game) < self.max_game_on_the_table:
            game = Game()
            self.game.append(game)
            return game

    def stop_the_game(self, game):
        return self.game.pop(game)

    def join_to_the_table(self, person):
        if person not in self.person_at_the_table:
            self.person_at_the_table.append(person)

    def disconnect_person_by_table(self, person):
        if person in self.person_at_the_table:
            self.person_at_the_table.remove(person)

    def perosn_join_to_the_game(self, person, game):
        if person in self.person_at_the_table and game in self.game:
            return game.add_players(person)


# Peter, Lukas, and Arthur enters the casino
peter = Player('Piotr', 'Witkowski')
lukas = Player('Łukasz', 'Witkowski')
arthur = Player('Artur', 'Witkowski')
# They look at the table on north and see that the game is start
table = Table()

# walks over to the table
peter.join_the_table(table)
lukas.join_the_table(table)
arthur.join_the_table(table)

# omaha game start, and croupier ask who wont join the game
# peter and lukas join, but arthur only looking at
game = table.start_the_game()
table.perosn_join_to_the_game(person=peter, game=game)
table.perosn_join_to_the_game(person=lukas, game=game)

# the game start
# croupier giving cards to players and put 5 to the table
game.distribute_cards_to_players()

print(peter.card)
print(lukas.card)
print(game.card)
