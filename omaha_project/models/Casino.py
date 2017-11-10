from random import shuffle

from models.Table import Table
from models.Game import Game
from models.People.Croupier import Croupier
from models.People.PlayerNormal import PlayerNormal
from models.People.PlayerRandomEnd import PlayerRandomEnd


class Casino:
    def __init__(self, *, name: str, adress: str):
        self.name = name
        self.adress = adress

        self.croupier = []
        self.players = []

        self.tables = dict()

    def get_default_croupier(self):
        shuffle(self.croupier)
        for croupier in self.croupier:
            if not croupier.actual_table:
                return croupier

    def check_if_can_create_game(self, *, table: Table, croupier: Croupier, money_min_to_connect: float):
        if len(table.person_at_the_table) < 2:
            # is too small players by the table
            return None
        if croupier not in self.croupier:
            # your croupier not exists, we take default croupier in casino
            croupier = self.get_default_croupier()
        if not croupier:
            # no croupiers or everyone is busy
            return None

        # if player have money then add to game
        players_game = []
        for player in table.person_at_the_table:
            if player.check_money(money=money_min_to_connect):
                players_game.append(player)
        # if count of game players is less than 2 then game is not start
        if len(players_game) < 2:
            return False
        return (players_game, croupier)

    def create_game_omaha(self, *, table_name: str, croupier, money_min_to_connect: float) -> Game:
        if table_name not in self.tables:
            return None

        can_create = self.check_if_can_create_game(table=self.tables[table_name],
                                                   croupier=croupier,
                                                   money_min_to_connect=money_min_to_connect)
        if can_create:
            players_to_game, croupier = can_create
        else:
            return None

        game = Game(table=self.tables[table_name], croupier=croupier,
                    money_min_to_connect=money_min_to_connect, game_players=players_to_game)
        return game

    def add_player_to_table(self, *, name_table: str, player) -> Table:
        if name_table in self.tables and player in self.players:
            self.tables[name_table].join_to_the_table(player=player)
            return self.tables[name_table]

    def add_table(self, *, name) -> Table:
        table = Table(casino=self, name=name)
        self.tables[name] = table
        return table

    def add_player(self, *, name: str, surname: str, money: float, type: str):
        """
        Croupier go to casino and registers there
        Args:
            shuffle_last - kind of take card with deck. If true then he take last cart else
                           he take first card from deck
            type - type of player:
                    1. 'normal' - PlayerNormal
                    2. 'random' - PlayerRandomEnd
        """
        if type == 'normal':
            player = PlayerNormal(name=name, surname=surname, money=money)
        elif type == 'random':
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
