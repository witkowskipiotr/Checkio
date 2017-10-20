import unittest

from oreilly.find_friends import make_connection_networks, check_connection

class CheckioTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            [("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
              "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
             "scout2",
             "scout3"],
            [("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
              "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
             "dr101",
             "sscout"],
            [(),
             "dr101",
             "sscout"],
            [("dr101-mr99",),
             "dr101",
             "mr99"]
        ]
        self.result_check_connection = [True, False, False, True]
        self.result_make_connection = [
            ({'dr101', 'mr99', 'out00'}, {'scout1', 'scout2', 'scout4', 'super', 'scout3', 'sscout'}),
            ({'dr101', 'mr99', 'out00'}, {'scout1', 'scout2', 'scout4', 'super', 'scout3', 'sscout'}),
            (),
            ({'dr101', 'mr99'},)
        ]

    def test_check_connection_equal(self):
        for i, (network, first, second) in enumerate(self.data):
            self.assertEqual(check_connection(network, first, second), self.result_check_connection[i])

    def test_make_connection_networks_equal(self):
        for i, data in enumerate(self.data):
            self.assertEqual(make_connection_networks(network=data[0]), self.result_make_connection[i])
