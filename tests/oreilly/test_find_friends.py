import unittest

from oreilly.find_friends import check_connection_between_users


class CheckioTest(unittest.TestCase):

    def test_check_connection_equal(self):
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

        for i, (network, first, second) in enumerate(self.data):
            self.assertEqual(check_connection_between_users(network=network,
                                                            first_user=first,
                                                            second_user=second),
                             self.result_check_connection[i])
