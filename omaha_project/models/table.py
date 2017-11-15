"""class Table"""
class Table:
    """
    The table can be approached by many people, but at one table can be only two games.
    To play must be at the table.
    Args:
        casino: class casino where is the table
        name: string of name - id table
    Example:
        mike -> player class
        table = Table(casino=casino, name='Green', max_number_of_players=3)
        table.join_to_the_table(player=mike)
        table.disconnect_by_table(player=mike)
    """
    def __init__(self, *, casino, name: str, max_number_of_players: int):

        self.person_at_the_table = []
        self.max_number_of_players = max_number_of_players
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
        player.actual_table = self
        return True

    def disconnect_by_table(self, *, player):
        """when the person resigns from the table"""
        if player in self.person_at_the_table:
            self.person_at_the_table.remove(player)
            player.actual_table = None
