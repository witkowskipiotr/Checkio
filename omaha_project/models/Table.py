class Table:
    """
    The table can be approached by many people, but at one table can be only two games.
    To play must be at the table.
    """
    def __init__(self, *, casino, name):
        self.person_at_the_table = []
        self.max_number_of_players = 2
        self.casino = casino
        self.name = name
        self.game = None
        self.money_min_to_connect = 2

    def join_to_the_table(self, *, player) -> bool:
        """when the person approaches the table he is append to the table"""
        if len(self.person_at_the_table) >= self.max_number_of_players:
            return False
        if player not in self.casino.players:
            return False
        if player in self.person_at_the_table:
            return False
        if player.money < self.money_min_to_connect:
            return False

        self.person_at_the_table.append(player)
        return True

    def disconnect_by_table(self, *, player):
        """when the person resigns from the table"""
        if player in self.person_at_the_table:
            self.person_at_the_table.remove(player)





    #
    #
    #
    # def start_the_game(self) -> Game:
    #     """initialize game"""
    #     if len(self.game) < self.max_game_on_the_table:
    #         game = Game()
    #         self.game.append(game)
    #         return game
    #
    # def stop_the_game(self, *, game: Game):
    #     """remove game from table"""
    #     return self.game.pop(game)
    #
    # def perosn_join_to_the_game(self, *, person: Player, game: Game) -> bool:
    #     """If an existing person wants to join the game must be at the table."""
    #     if person in self.person_at_the_table and game in self.game:
    #         game.add_players(player=person)
    #         return True
    #
    #
    #
    # def add_players(self, *, player: Player, money: float) -> bool:
    #     """add person to the game if is the required number of cards in the deck"""
    #     if player not in self.players and len(self.players) < self.max_amount_player:
    #         if player.money < money:
    #             return False
    #         else:
    #             player.spend_money(money=money)
    #             self.__rate_of_the_game += money
    #
    #         self.players.append(player)
    #         # add player to list who play the game
    #         player.join_the_game(self)
    #         return True
    #
    # def remove_players_from_game(self, *, player: Player):
    #     """When person aut of game"""
    #     if player in self.players:
    #         self.players.remove(player)
    #         # remove player to list who play the game
    #         player.game.remove(player)
    #
    #
    #
    # def get_rate_of_the_game(self):
    #     """get velue by variable self.__rate_of_the_game"""
    #     return self.__rate_of_the_game