from unittest import TestCase, main
from project.player.beginner import Beginner


class TestBeginer(TestCase):
    def setUp(self):
        self.pl = Beginner("Beg")

    def test_init_correct(self):
        self.assertEqual("Beg", self.pl.username)
        self.assertEqual(50, self.pl.health)
        self.assertEqual("CardRepository", self.pl.card_repository.__class__.__name__)

    def test_init_incorrect_name(self):
        with self.assertRaises(Exception) as ex:
            self.pl.username = ""
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_init_incorrect_health(self):
        with self.assertRaises(Exception) as ex:
            self.pl.health = -1
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_is_dead_is_true(self):
        self.pl.health = 0
        self.assertTrue(self.pl.is_dead)

    def test_is_dead_is_false(self):
        self.assertFalse(self.pl.is_dead)

    def test_take_damage_correct(self):
        self.pl.take_damage(10)
        self.assertEqual(40, self.pl.health)

    def test_take_damage_incorrect(self):
        with self.assertRaises(Exception) as ex:
            self.pl.take_damage(-10)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))


if __name__ == "__main__":
    main()
