from project.player.player_repository import PlayerRepository
from project.player.beginner import Beginner
from unittest import TestCase, main


class TestPlayerRepository(TestCase):
    def setUp(self):
        self.pr = PlayerRepository()

    def test_init(self):
        self.assertEqual(0, self.pr.count)
        self.assertEqual([], self.pr.players)

    def test_add_correct(self):
        pl_b = Beginner('beg')
        self.pr.add(pl_b)
        self.assertEqual(1, self.pr.count)
        self.assertEqual([pl_b], self.pr.players)

    def test_add_incorrect(self):
        pl_b = Beginner('beg')
        self.pr.add(pl_b)
        with self.assertRaises(Exception) as ex:
            self.pr.add(pl_b)
        self.assertEqual("Player beg already exists!", str(ex.exception))

    def test_remove_correct(self):
        pl_b = Beginner('beg')
        self.pr.add(pl_b)
        self.pr.remove("beg")
        self.assertEqual(0, self.pr.count)
        self.assertEqual([], self.pr.players)

    def test_remove_incorrect(self):
        with self.assertRaises(Exception) as ex:
            self.pr.remove("")
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))
        self.assertEqual(0, self.pr.count)
        self.assertEqual([], self.pr.players)

    def test_find(self):
        pl_b = Beginner('beg')
        self.pr.add(pl_b)
        self.assertEqual(pl_b, self.pr.find('beg'))


if __name__ == "__main__":
    main()
