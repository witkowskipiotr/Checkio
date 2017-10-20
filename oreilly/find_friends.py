# -*- coding: utf-8 -*-
"""
O'Reilyy functions from
https://py.checkio.org/mission/find-friends/
"""

def make_connection_networks(network: tuple) -> tuple:
    """
    We create networks with connections between users
    :param network: all connections between users
    return: network if all are connected in one
            Networks created from independent connections
    """
    #
    # networks = set()
    # for connection in network:
    #     networks.add(connection)
    #     user_1, user_2 = connection.split("-")
    #     for i, conn in enumerate(network):
    #         user_1_check, user_2_check = conn.split("-")
    #         if user_2 == user_1_check:
    #             networks.add(user_1 + "-" + user_2_check)
    #         if user_1 == user_2_check:
    #             networks.add(user_2 + "-" + user_1_check)
    # network = tuple(networks)
    # networks = set()
    # for connection in network:
    #     networks.add(connection)
    #     user_1, user_2 = connection.split("-")
    #     for i, conn in enumerate(network):
    #         user_1_check, user_2_check = conn.split("-")
    #         if user_2 == user_1_check:
    #             networks.add(user_1 + "-" + user_2_check)
    #         if user_1 == user_2_check:
    #             networks.add(user_2 + "-" + user_1_check)
    #
    # return tuple(networks)
    pass

def make_connection_networks1(network: tuple, first: str, second: str) -> tuple:
    networks = []
    for connection in network:
        user_1, user_2 = connection.split("-")
        is_conn_in_network = False
        networks.append({user_1, user_2})
        for i, conn in enumerate(networks):
            if user_1 in conn or user_2 in conn:
                networks[i].add(user_1)
                networks[i].add(user_2)
                is_conn_in_network = True
    return tuple(networks)


def check_connection(network: tuple, first: str, second: str) -> bool:
    for net in make_connection_networks1(network, first, second):
        if first in net and second in net:
            return True
    return False

a = check_connection(("nikola-robin","batman-nwing","mr99-batman","mr99-robin","dr101-out00","out00-nwing",),
                     "dr101","mr99")
print(a)
#
# def make_connection_networks(network: tuple) -> tuple:
#     """
#     We create networks with connections between users
#     :param network: all connections between users
#     return: network if all are connected in one
#             Networks created from independent connections
#     """
#     networks = set()
#     for connection in network:
#         networks.add(connection)
#         user_1, user_2 = connection.split("-")
#         for i, conn in enumerate(network):
#             user_1_check, user_2_check = conn.split("-")
#             if user_2 == user_1_check:
#                 networks.add(user_1 + "-" + user_2_check)
#     return tuple(networks)
#
#
#
# def check_connection(network: tuple, first: str, second: str) -> bool:
#
#     print(make_connection_networks(network), str(first) + "-" + str(second))
#     return str(first) + "-" + str(second) in make_connection_networks(network)



assert check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True, "Scout Brotherhood"
assert check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "super", "scout2") == True, "Super Scout"
assert check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False, "I don't know any scouts."

assert check_connection(("nikola-robin","batman-nwing","mr99-batman",
                          "mr99-robin","dr101-out00","out00-nwing",),
    "dr101","mr99") == True, 'ok'


d = check_connection(("nikola-robin", "batman-nwing", "mr99-batman", "mr99-robin", "dr101-out00", "out00-nwing",),
                 "dr101",
                 "mr99")

print(d)

#print(a, b, c)