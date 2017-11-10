from models.People.Player import Player


class PlayerNormal(Player):
    """Player play to the end of the game"""
    def __init__(self, *, name: str, surname: str, money: float):
        super().__init__(name=name, surname=surname, money=money)
        #Player play to the end of the game
        self.when_finish_game = 0