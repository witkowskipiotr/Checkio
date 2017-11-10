from models.People.Person import Person

class Player(Person):

    def __init__(self, *, name: str, surname: str, money: float):
        super().__init__(name=name, surname=surname)
        self.money = round(money, 2)
        self.amount_win = 0
        self.amount_lose = 0

    def add_money(self, *, money: float):
        """When person win money or get from bank, his wallet up"""
        self.money += round(money, 2)

    def spend_money(self, *, money: float) -> bool:
        """when person buy drink or raises the stake by game"""
        if self.check_money(money=money):
            self.money -= round(money, 2)
            return True
        return False

    def check_money(self, *, money: float) -> bool:
        """when person buy drink or raises the stake by game"""
        if self.money >= money:
            return True
        return False
