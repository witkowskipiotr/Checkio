# -*- coding: utf-8 -*-
"""
O'Reilyy functions from
https://py.checkio.org/mission/find-friends/
"""


def check_connection(network, first, second):
    connects = []
    for node in network:
        connects.append(set(node.split('-')))

    for i in range(len(connects) - 1):
        for j in range(i + 1, len(connects)):
            if connects[i] & connects[j]:
                connects[j] |= connects[i]
                connects[i].clear()
                break
    for connect in connects:
        if first in connect and second in connect:
            return True
    return False
