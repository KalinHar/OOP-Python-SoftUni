from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Kas", 1, 5.5, 7.5)

    def test_init(self):
        self.assertEqual("Kas", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(5.5, self.hero.health)
        self.assertEqual(7.5, self.hero.damage)

    def test_string_repr(self):
        self.assertEqual("Hero Kas: 1 lvl\nHealth: 5.5\nDamage: 7.5\n",
                         self.hero.__str__())

    def test_battle_with_same_name(self):
        en_hero = Hero("Kas", 1, 5.5, 7.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(en_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_self_low_health(self):
        enemy_hero = Hero("Tor", 1, 5.5, 7.5)
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest",
                         str(ex.exception))

    def test_battle_enemy_low_health(self):
        enemy_hero = Hero("Tor", 1, 0, 7.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight Tor. He needs to rest",
                         str(ex.exception))

    def test_correct_battle_with_draw(self):
        enemy_hero = Hero("Tor", 1, 7.5, 6.5)
        self.assertEqual("Draw", self.hero.battle(enemy_hero))

    def test_correct_battle_with_win(self):
        enemy_hero = Hero("Tor", 1, 7.5, 4.5)
        self.assertEqual("You win", self.hero.battle(enemy_hero))
        self.assertEqual(2, self.hero.level)
        self.assertEqual(6, self.hero.health)
        self.assertEqual(12.5, self.hero.damage)

    def test_correct_battle_with_lose(self):
        enemy_hero = Hero("Tor", 1, 8.5, 4.5)
        self.assertEqual("You lose", self.hero.battle(enemy_hero))
        self.assertEqual(2, enemy_hero.level)
        self.assertEqual(6, enemy_hero.health)
        self.assertEqual(9.5, enemy_hero.damage)


if __name__ == "__main__":
    main()