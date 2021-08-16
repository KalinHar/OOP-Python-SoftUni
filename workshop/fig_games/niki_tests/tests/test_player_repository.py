import unittest

from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class PlayerRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.beginner = Beginner('TestBeginner')
        self.advanced = Advanced('TestAdvanced')
        self.pr = PlayerRepository()

    def test_player_repository_has_correct_attr_when_initialized(self):
        self.assertEqual([], self.pr.players)
        self.assertEqual(0, self.pr.count)

    def test_player_repository_can_add_single_player(self):
        self.pr.add(self.beginner)
        self.assertEqual(1, len(self.pr.players))
        self.assertEqual(1, self.pr.count)
        self.assertIn(self.beginner, self.pr.players)

    def test_player_repository_can_add_multiple_players(self):
        self.pr.add(self.beginner)
        self.pr.add(self.advanced)
        self.assertEqual(2, len(self.pr.players))
        self.assertEqual(2, self.pr.count)
        self.assertIn(self.beginner, self.pr.players)
        self.assertIn(self.advanced, self.pr.players)

    def test_player_repository_raises_when_adding_same_player_twice(self):
        self.pr.add(self.beginner)
        with self.assertRaises(ValueError) as context:
            self.pr.add(self.beginner)
        msg = "Player TestBeginner already exists!"
        self.assertEqual(msg, str(context.exception))

    def test_player_repository_removes_player_correctly(self):
        self.pr.add(self.beginner)
        self.pr.add(self.advanced)
        self.assertIn(self.beginner, self.pr.players)
        self.assertIn(self.advanced, self.pr.players)
        self.pr.remove('TestBeginner')
        self.assertEqual(1, self.pr.count)
        self.assertIn(self.advanced, self.pr.players)
        self.assertNotIn(self.beginner, self.pr.players)

    def test_player_repository_raises_when_removing_empty_name(self):
        self.pr.add(self.beginner)
        with self.assertRaises(ValueError) as context:
            self.pr.remove('')
        msg = "Player cannot be an empty string!"
        self.assertEqual(msg, str(context.exception))

    def test_player_repository_does_nothing_when_removing_non_present_player(self):
        self.pr.add(self.beginner)
        self.pr.remove('TestAdvanced')
        self.assertEqual(1, self.pr.count)

    def test_user_repository_finds_correct_player(self):
        self.pr.add(self.beginner)
        self.pr.add(self.advanced)
        p = self.pr.find('TestBeginner')
        self.assertEqual(p, self.beginner)

    def test_user_repository_find_returns_none_when_search_unsuccessful(self):
        self.pr.add(self.advanced)
        p = self.pr.find('TestBeginner')
        self.assertEqual(p, None)



if __name__ == "__main__":
    unittest.main()
