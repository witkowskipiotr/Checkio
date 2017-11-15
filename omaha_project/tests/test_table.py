import unittest

from models.casino import Casino
from models.table import Table


class TableTest(unittest.TestCase):

    def setUp(self):
        # initialize person
        self.casino = Casino(name='Cristal Casino', adress='Królewska 11, Warszawa')
        # create croupier
        self.croupier = self.casino.add_croupier(name='Grzegorz',
                                                 surname='Brzęczyszczykiewicz',
                                                 shuffle_last=True)
        # create players
        self.mike = self.casino.add_player(name='Michał', surname='Nowak',
                                           money=10, type_player='random')
        self.peter = self.casino.add_player(name='Piotr', surname='Witkowski',
                                            money=100.52, type_player='random')

    def test_create_table(self):

        self.table_green = Table(casino=self.casino, name='Green', max_number_of_players=4)
        self.assertEqual(self.table_green.casino, self.casino)
        self.assertEqual(self.table_green.name, 'Green')
        self.assertEqual(self.table_green.max_number_of_players, 4)
        self.assertEqual(len(self.table_green.person_at_the_table), 0)

    def test_join_croupier_to_the_table(self):
        # nobody is by the table
        self.table_green = Table(casino=self.casino, name='Green', max_number_of_players=4)

        self.assertEqual(len(self.table_green.person_at_the_table), 0)
        # croupier not join to the table because he is empolyee
        self.table_green.join_to_the_table(player=self.croupier)
        # mike not in table
        self.assertNotIn(self.croupier, self.table_green.person_at_the_table)
        self.assertEqual(len(self.table_green.person_at_the_table), 0)

    def test_join_to_the_table(self):

        self.table_green = Table(casino=self.casino, name='Green', max_number_of_players=4)
        # add first player to the table
        self.table_green.join_to_the_table(player=self.mike)
        self.assertEqual(len(self.table_green.person_at_the_table), 1)
        self.assertIn(self.mike, self.table_green.person_at_the_table)
        # add another player
        self.table_green.join_to_the_table(player=self.peter)
        self.assertEqual(len(self.table_green.person_at_the_table), 2)
        self.assertIn(self.mike, self.table_green.person_at_the_table)
        self.assertIn(self.peter, self.table_green.person_at_the_table)

    def test_disconnect_by_table(self):

        self.table_green = Table(casino=self.casino, name='Green', max_number_of_players=4)
        # join two player in table
        self.table_green.join_to_the_table(player=self.mike)
        self.table_green.join_to_the_table(player=self.peter)
        # two player in table
        self.assertEqual(len(self.table_green.person_at_the_table), 2)
        # disconnect player by table
        self.table_green.disconnect_by_table(player=self.mike)
        # mike not in table
        self.assertNotIn(self.mike, self.table_green.person_at_the_table)
        # ony one player in table
        self.assertEqual(len(self.table_green.person_at_the_table), 1)
        # peter still in table
        self.assertIn(self.peter, self.table_green.person_at_the_table)
