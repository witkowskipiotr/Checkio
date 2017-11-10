import unittest
from omaha import Table

class TableTest(unittest.TestCase):

    def setUp(self):
        # initialize person
        self.gregor = Player(name='Grzegorz', surname='Brzęczyszczykiewicz', money=0)
        self.mike = Player(name='Michał', surname='Nowak', money=10)
        self.peter = Player(name='Piotr', surname='Witkowski', money=100)
        self.lukas = Player(name='Łukasz', surname='Witkowski', money=100)
        self.arthur = Player(name='Artur', surname='Witkowski', money=100)
        # create tree table
        self.table_green = Table()
        self.table_blue = Table()
        self.table_red = Table()
        # create two game by one table
        self.green_omaha_one = self.table_green.start_the_game()
        self.green_omaha_two = self.table_green.start_the_game()

    def test_person_join_table(self):
        self.peter.join_the_table(table=self.table_green)

        # check than peter is by table green
        self.assertTrue(self.peter.actual_table)
        self.assertTrue(self.peter.actual_table == self.table_green)

        # check than by table is peter
        self.assertIn(self.peter, self.table_green.person_at_the_table, "Peter is not by the table")

    def test_person_not_in_table(self):
        self.assertNotEqual(self.peter.actual_table, self.table_green)
        self.assertNotIn(self.peter, self.table_green.person_at_the_table)
        self.peter.join_the_table(table=self.table_red)
        self.assertNotEqual(self.peter.actual_table, self.table_green)
        self.assertNotIn(self.peter, self.table_green.person_at_the_table)

    def test_person_is_in_table(self):
        self.assertNotEqual(self.peter.actual_table, self.table_green)
        self.assertNotIn(self.peter, self.table_green.person_at_the_table)
        self.peter.join_the_table(table=self.table_green)
        self.assertEqual(self.peter.actual_table, self.table_green)
        self.assertIn(self.peter, self.table_green.person_at_the_table)

    def test_persons_is_in_table_and_migrate_table(self):
        self.peter.join_the_table(table=self.table_green)
        self.mike.join_the_table(table=self.table_green)
        self.gregor.join_the_table(table=self.table_green)
        self.lukas.join_the_table(table=self.table_green)
        self.arthur.join_the_table(table=self.table_green)
        self.arthur.join_the_table(table=self.table_red)

        # check than person is by the table
        self.assertIn(self.peter, self.table_green.person_at_the_table)
        self.assertIn(self.mike, self.table_green.person_at_the_table)
        self.assertIn(self.gregor, self.table_green.person_at_the_table)
        self.assertIn(self.lukas, self.table_green.person_at_the_table)
        self.assertIn(self.arthur, self.table_green.person_at_the_table)
        self.assertIn(self.arthur, self.table_red.person_at_the_table)

        # check than person is actual by table
        self.assertEqual(self.peter.actual_table, self.table_green)
        self.assertEqual(self.mike.actual_table, self.table_green)
        self.assertEqual(self.gregor.actual_table, self.table_green)
        self.assertEqual(self.lukas.actual_table, self.table_green)
        self.assertEqual(self.arthur.actual_table, self.table_red)

        # arthur is by the table_red and table_gree, but actual is only by table red
        self.assertNotEqual(self.arthur.actual_table, self.table_green)

        # arthur go to table_green
        self.arthur.log_in_table(table=self.table_green)
        self.assertNotEqual(self.arthur.actual_table, self.table_red)
        self.assertEqual(self.arthur.actual_table, self.table_green)
        self.assertIn(self.arthur, self.table_green.person_at_the_table)
        self.assertIn(self.arthur, self.table_red.person_at_the_table)