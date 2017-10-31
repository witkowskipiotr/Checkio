# -*- coding: utf-8 -*-
"""
O'Reilly functions from
https://py.checkio.org/mission/friends/
"""


class Friends:
    """
    Returns a new Friends instance. "connections" is an iterable of sets with two elements in each.
    Each connection contains two names as strings. Connections can be repeated in the initial data,
    but inside it's stored once. Each connection has only two states - existing or not.
    """
    def __init__(self, connections: list or tuple):
        self.__frends = list(connections) \
            if isinstance(connections, (list, tuple)) else [connections]

    def check_connection(self, connection):
        return True if connection in self.__frends else False

    def add_connection(self, connection: set) -> bool:
        is_in_connection = self.check_connection(connection)
        if not is_in_connection:
            self.__frends.append(connection)
        return not is_in_connection

    def remove_connection(self, connection: set) -> bool:
        is_in_connection = self.check_connection(connection)
        if is_in_connection:
            self.__frends.remove(connection)
        return is_in_connection

    def names_of_all_connection(self) -> set:
        """
        :return: all elements as a list
        """
        name = set()
        [name.add(c) for conn in self.__frends for c in conn]
        return name

    def connected(self, name_connected: str) -> set:
        """
        checks the connection for the item
        """
        name = [c for conn in self.__frends
                for c in conn if c != name_connected and name_connected in conn]
        return set(name)
