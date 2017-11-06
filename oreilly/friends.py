# -*- coding: utf-8 -*-
"""
O'Reilly functions from https://py.checkio.org/mission/friends/
"""


class Friends:
    """
    class is responsobile for keeping relations between friends.
    Each connection contains two names as strings. Connections can be repeated in the initial data,
    but inside it's stored once. Each connection has only two states - existing or not.
    """
    def __init__(self, connections: list or tuple):
        """
        Args:
            connections: list or tuple of connections set between two user
        for example:
            Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
            Friends([{"1", "2"}, {"3", "1"}])
        """
        self.__frends = list(connections) \
            if isinstance(connections, (list, tuple)) else [connections]

    def check_connection(self, connection):
        """
        Slave function chall in function:
        - remove_connection
        - add_connection
        We check that the set of two names is exists in list friends.
        for example:
            f = Friends([{"1", "2"}, {"3", "1"}])
            f.check_connection({"1", "3"}) -> True
            f.check_connection({"4", "5"}) -> False
        """
        return True if connection in self.__frends else False

    def add_connection(self, connection: set) -> bool:
        """
        Add a connection in the instance. "connection" is a set of two names (strings).
        Returns True if this connection is new. Returns False if this connection exists already.
        for example:
            f = Friends([{"1", "2"}, {"3", "1"}])
            f.add({"1", "3"}) -> False
            f.add({"4", "5"}) -> True
        """
        is_in_connection = self.check_connection(connection=connection)
        if not is_in_connection:
            self.__frends.append(connection)
        return not is_in_connection

    def remove_connection(self, connection: set) -> bool:
        """
        Remove a connection from the instance. "connection" is a set of two names (strings).
        Returns True if this connection exists, False if this connection is not in the instance.
        for example:
            f = Friends([{"1", "2"}, {"3", "1"}])
            f.remove({"1", "3"}) -> True
            f.remove({"4", "5"}) -> False
        """
        is_in_connection = self.check_connection(connection=connection)
        if is_in_connection:
            self.__frends.remove(connection)
        return is_in_connection

    def names_of_all_connection(self) -> set:
        """
        Returns a set of names. The set contains only names which are connected with somebody.
        for example:
            f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
            f.names_of_all_connection() -> {"a", "b", "c", "d"}
            f.remove({"d", "c"}) -> True
            f.names_of_all_connection() -> {"a", "b", "c"}
        """
        return set([name for conn in self.__frends for name in conn])

    def connected(self, name_connected: str) -> set:
        """
        Returns a set of names which is connected with the given "name".
        If "name" does not exist in the instance, then return an empty set.
        for example:
            f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
            f.connected("a") -> {"b", "c"}
            f.connected("d") -> set()
            f.remove({"c", "a"}) -> True
            f.connected("c") -> {"b"}
            f.remove({"c", "b"}) -> True
            f.connected("c") -> set()
        """
        return set([name for conn in self.__frends for name in conn
                    if name != name_connected and name_connected in conn])
