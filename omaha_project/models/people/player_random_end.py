from models.people.player import Player
from random import shuffle


class PlayerRandomEnd(Player):
    def __init__(self, *, name: str, surname: str, money: float):
        """
        Player play to random step game
        0 - play to the end
        1,2,3,... - step when finish
        """
        super().__init__(name=name, surname=surname, money=money)
        step = [0, 1, 2, 3, 4]
        shuffle(step)
        self.when_finish_game = step[0]
