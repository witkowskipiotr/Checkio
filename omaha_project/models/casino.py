"""
casino include many people, tables and game
"""

from random import shuffle

from models.table import Table
from models.game import Game
from models.people.croupier import Croupier
from models.people.player_normal import PlayerNormal
from models.people.player_random_end import PlayerRandomEnd


class Casino:
    """casino include many people, tables and game
    ::
        Example call
            casino = Casino(name='Royal Casino', adress='Warszawska 1, Warszawa')
            gregor = casino.add_croupier(name='Grzegorz',
                                         surname='Brzęczyszczykiewicz',
                                         shuffle_last=True)
            mike = casino.add_player(name='Michał', surname='Nowak',
                                     money=10, type_player='random')
            peter = casino.add_player(name='Piotr', surname='Witkowski',
                                      money=100.52, type_player='random')
            table_green = casino.add_table(name='Green', max_number_of_players=3)
            casino.add_player_to_table(name_table='Green', player=mike)
            casino.add_player_to_table(name_table='Green', player=peter)
            game = casino.create_game_omaha(table_name='Green', croupier=gregor,
                                                 money_min_to_connect=1)
        The game plays in game
        """
    def __init__(self, *, name: str, adress: str):
        self.name = name
        self.adress = adress
        self.croupier = []
        self.players = []
        self.tables = dict()

    def get_default_croupier(self):
        """
        We choose the croupier from the free crupiers in the casino
        """
        shuffle(self.croupier)
        for croupier in self.croupier:
            if not croupier.actual_table:
                return croupier

    def check_if_can_create_game(self, *, table_name: str, croupier: Croupier,
                                 money_min_to_connect: float):
        """
        slave function called in create_game_omaha
        Return:
            False if available players is to small or all croupier is busy.
            If we can create game return list of players game and croupier who runs a game
        """

        if table_name not in self.tables:
            return None, None
        table = self.tables[table_name]

        if len(table.person_at_the_table) < 2:
            # is too small players by the table
            return None, None
        if croupier not in self.croupier:
            # your croupier not exists, we take default croupier in casino
            croupier = self.get_default_croupier()
        if not croupier:
            # no croupiers or everyone is busy
            return None, None

        # if player have money then add to game
        players_game = []
        for player in table.person_at_the_table:
            if player.check_money(money=money_min_to_connect):
                players_game.append(player)
        # if count of game players is less than 2 then game is not start
        if len(players_game) < 2:
            return False, None
        return players_game, croupier

    def create_game_omaha(self, *, table_name: str, croupier: Croupier,
                          money_min_to_connect: float) -> Game:
        """
        Create new game
        Args:
            money_min_to_connect: The minimum rate a player must have in order to enter the game.
        """
        players_to_game, croupier = self.check_if_can_create_game(
            table_name=table_name, croupier=croupier,
            money_min_to_connect=money_min_to_connect)
        if players_to_game:
            # Create game
            game = Game(table=self.tables[table_name], croupier=croupier,
                        money_min_to_connect=money_min_to_connect, game_players=players_to_game)
            return game

    def add_player(self, *, name: str, surname: str, money: float, type_player: str):
        """
        Croupier go to casino and registers there
        Args:
            shuffle_last - kind of take card with deck. If true then he take last cart else
                           he take first card from deck
            type - type of player:
                    1. 'normal' - PlayerNormal
                    2. 'random' - PlayerRandomEnd
        """
        if type_player == 'normal':
            player = PlayerNormal(name=name, surname=surname, money=money)
        elif type_player == 'random':
            player = PlayerRandomEnd(name=name, surname=surname, money=money)
        else:
            return
        self.players.append(player)
        return player

    def del_player(self, player):
        """When croupier out of the casino"""
        if player in self.players:
            self.players.remove(player)
            del player

    def add_table(self, *, name: str, max_number_of_players: int) -> Table:
        """Add to list new table"""
        table = Table(casino=self, name=name, max_number_of_players=max_number_of_players)
        self.tables[name] = table
        return table

    def del_table(self, *, name: str):
        """Delete table in tables"""
        if name in self.tables:
            del self.tables[name]

    def add_player_to_table(self, *, name_table: str, player) -> Table:
        """Add to list new player"""
        if name_table in self.tables and player in self.players:
            self.tables[name_table].join_to_the_table(player=player)
            return self.tables[name_table]

    def del_player_from_table(self, *, name_table: str, player):
        """Del player from table"""
        if name_table in self.tables:
            self.tables[name_table].disconnect_by_table(player=player)

    def add_croupier(self, *, name: str, surname: str, shuffle_last: bool) -> Croupier:
        """
        Croupier go to casino and registers there
        Args:
            shuffle_last - kind of take card with deck. If true then he take last cart else
            he take first card from deck
        """
        croupier = Croupier(name=name, surname=surname, shuffle_last=shuffle_last)
        self.croupier.append(croupier)
        return croupier

    def del_croupier(self, croupier):
        """When croupier out of the casino"""
        if croupier in self.croupier:
            self.croupier.remove(croupier)
            del croupier
