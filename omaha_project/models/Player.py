from models import Table

class Player:
    """
    class of person player
    When person into the casino class is create, but he
    dies bit have join the game immediately (maybe he wants to drink first)
    """

    def __init__(self, *, name: str, surname: str, money: float):
        self.name = name
        self.surname = surname
        self.money = money
        self.cards = []
        self.game = []
        self.actual_table = None

    def log_in_table(self, *, table: Table) -> bool:
        """If person return to the table where is login"""
        if self in table.person_at_the_table:
            self.actual_table = table
            return True

    def join_the_table(self, *, table: Table):
        """One person can be only by one table"""
        if table._person_join_to_the_table(person=self):
            self.actual_table = table

    def out_the_table(self, *, table: Table):
        """One person can be only by one table"""
        if self in table.person_at_the_table:
            table.person_at_the_table.remove(self)

    def join_the_game(self, game: Game):
        """When person join game his cards is create"""

        self.game.append(game)
        self.cards = {1: '', 2: '', 3: '', 4: ''}

    # def out_the_game(self):
    #     """When person aut of game his cards removed"""
    #     self.cards = []

    def person_add_money(self, *, money: float):
        """When person win money or get from bank, his wallet up"""
        self.money += round(money, 2)

    def spend_money(self, *, money: float):
        """when person buy drink or raises the stake by game"""
        self.money -= round(money, 2)
