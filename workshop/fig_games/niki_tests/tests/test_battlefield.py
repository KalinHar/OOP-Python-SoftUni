import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class BattleFieldTests(unittest.TestCase):
    def setUp(self) -> None:
        self.c = MagicCard('Test')
        self.p1 = Beginner('Player1')
        self.p2 = Advanced('Player2')
        self.bf = BattleField()

    def test_fight_returns_player_correct_info(self):
        self.p1.card_repository.add(self.c)
        self.p2.card_repository.add(self.c)
        self.bf.fight(self.p1, self.p2)
        self.assertEqual(135, self.p1.health)
        self.assertEqual(295, self.p2.health)

    def test_fight_raises_when_start_with_dead_player(self):
        self.p1.card_repository.add(self.c)
        self.p1.health = 0
        self.p2.card_repository.add(self.c)
        with self.assertRaises(ValueError) as ctx:
            self.bf.fight(self.p1, self.p2)
        expected_message = "Player is dead!"
        self.assertEqual(expected_message, str(ctx.exception))
        self.assertEqual(250, self.p2.health)
        self.assertEqual(0, self.p1.health)

    # def test_fight_raised_message(self):
    #     self.p1.card_repository.add(self.c)
    #     self.p1.card_repository.add(self.c)
    #     self.p2.card_repository.add(self.c)
    #     with self.assertRaises(Exception) as ex:
    #         self.bf.fight(self.p1, self.p2)
    #     self.assertEqual("Player's health bonus cannot be less than zero.",
    #                      str(ex.exception))


if __name__ == "__main__":
    unittest.main()
