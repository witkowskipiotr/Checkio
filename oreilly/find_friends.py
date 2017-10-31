# -*- coding: utf-8 -*-
"""
O'Reilly functions from
https://py.checkio.org/mission/find-friends/
"""


def check_connection(network, first, second):
    """
    allow determine more complex connection between two users.
    :param network: tuple of connection user
    :param first, second: user to check connection together
    :return: True if connection is possible
    """
    connects = []
    for node in network:
        connects.append(set(node.split('-')))

    for i in range(len(connects) - 1):
        for j in range(i + 1, len(connects)):
            print(connects[i], connects[j])
            if connects[i] & connects[j]:
                connects[j] |= connects[i]
                connects[i].clear()
                break
    for connect in connects:
        if first in connect and second in connect:
            return True
    return False
