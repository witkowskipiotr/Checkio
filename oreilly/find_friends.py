# -*- coding: utf-8 -*-
"""
O'Reilly functions from
https://py.checkio.org/mission/find-friends/
"""


def find_path(graph, start, end, path=[]):
    """
    Takes a graph and the start and end nodes as arguments. It will return a list of nodes
    (including the start and end nodes) comprising the path. When no path can be found,
    it returns None. The same node will not occur more than once on the path returned
    (i.e. it won't contain cycles). The algorithm uses an important technique
    called backtracking: it tries each possibility in turn until it finds a solution.
    Args:
        graph: networks consisting of nodes connected
        start: first item in network check
        end: last item in network check
        path: we need it in recursion - this is create path in two nodes
    return: if is network in start and end node we get path between both else we get None
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            path_new = find_path(graph, node, end, path)
            if path_new:
                return path_new
    return None


def check_connection_between_users(network: tuple, first_user: str, second_user: str) -> bool:
    """
    allow determine more complex connection between two users.
    Args:
        network: tuple of connection user
        first_user, second_user: user to check connection together
    return:
        True if connection is possible
    example network:
        check_connection(
            ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
             "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
             "scout2",
             "scout3") -> True
        check_connection(
            ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
             "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
             "dr101",
             "sscout") -> False
    """
    graph = {}
    for node in network:
        user_1, user_2 = node.split('-')
        for iterable in range(2):
            # include into graph as many variables as there are unique points in the network
            # so that we can check all connections
            # duplicate - write two variables to graph as key
            # If we did not do this: a-b, b-c can not find c in the node and raise error
            if user_1 not in graph:
                graph[user_1] = [user_2]
            elif user_2 not in graph[user_1]:
                graph[user_1].append(user_2)
            if iterable == 0:
                # exchange of variable values to
                user_1_help = user_1
                user_1 = user_2
                user_2 = user_1_help
    result = find_path(graph=graph, start=first_user, end=second_user)
    return True if result else False
