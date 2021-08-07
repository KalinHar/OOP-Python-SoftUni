from project.battle_field import BattleField
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.trap_card import TrapCard
from project.card.magic_card import MagicCard
from unittest import TestCase, main


class TestBattleField(TestCase):
    def setUp(self):
        self.b = BattleField
        self.att_b = Beginner("atb")
        self.att_a = Advanced("ata")
        self.en_b = Beginner("enb")
        self.en_a = Advanced("ena")

    def test_fight_dead_attacker(self):
        self.att_b.health = 0
        with self.assertRaises(Exception) as ex:
            self.b.fight(self.att_b, self.en_a)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_fight_dead_enemy(self):
        self.en_a.health = 0
        with self.assertRaises(Exception) as ex:
            self.b.fight(self.att_b, self.en_a)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_fight_dead_both(self):
        self.att_b.health = 0
        self.en_a.health = 0
        with self.assertRaises(Exception) as ex:
            self.b.fight(self.att_b, self.en_a)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_fight_with_attacker_lose(self):
        cm = MagicCard("mag")
        ct = TrapCard("tra")
        self.att_b.card_repository.cards = [ct]
        self.en_a.card_repository.cards = [cm, ct]
        with self.assertRaises(Exception) as ex:
            self.b.fight(self.att_b, self.en_a)
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_fight_with_enemy_lose(self):
        cm = MagicCard("mag")
        ct = TrapCard("tra")
        self.att_a.card_repository.cards = [ct, cm, ct]
        self.en_b.card_repository.cards = [cm]
        with self.assertRaises(Exception) as ex:
            self.b.fight(self.att_a, self.en_b)
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_fight_correct(self):
        cm = MagicCard("mag")
        ct = TrapCard("tra")
        self.att_a.card_repository.cards = [cm]
        self.en_b.card_repository.cards = [ct]
        self.assertEqual(250, self.att_a.health)
        self.assertEqual(50, self.en_b.health)
        self.b.fight(self.att_a, self.en_b)
        self.assertEqual(180, self.att_a.health)
        self.assertEqual(90, self.en_b.health)
        self.assertEqual(150, ct.damage_points)
        self.assertEqual(5, cm.damage_points)


if __name__ == "__main__":
    main()
