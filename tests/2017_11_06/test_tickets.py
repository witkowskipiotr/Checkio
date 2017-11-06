import unittest

from code_2017_11_06.tickets import sell_tickets_to_all_customers


class SellTicketTest(unittest.TestCase):

    def test_can_sell_without_spend_the_rest(self):
        self.assertEqual(sell_tickets_to_all_customers(people=[25]), "YES")
        self.assertEqual(sell_tickets_to_all_customers(people=[25, 25, 25, 25, 25, 25, 25, 25, 25, 25]), "YES")

    def test_can_sell_with_spend_the_rest(self):
        self.assertEqual(sell_tickets_to_all_customers(people=[25, 50]), "YES")
        self.assertEqual(sell_tickets_to_all_customers(people=[25, 25, 50, 50]), "YES")

    def test_cant_sell(self):
        self.assertEqual(sell_tickets_to_all_customers(people=[25, 100]), "NO")
        self.assertEqual(sell_tickets_to_all_customers(people=[50]), "NO")
        self.assertEqual(sell_tickets_to_all_customers(people=[50, 25]), "NO")

    def test_cant_sell_with_spend_the_rest(self):
        # we don`t have bill to give rest
        self.assertEqual(sell_tickets_to_all_customers(people=[25, 50, 50]), "NO")
        self.assertEqual(sell_tickets_to_all_customers(people=[25, 50, 100]), "NO")
        self.assertEqual(sell_tickets_to_all_customers(people=[25, 25, 50, 50, 100]), "NO")
        self.assertEqual(sell_tickets_to_all_customers(
            people=[25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]), "NO")
