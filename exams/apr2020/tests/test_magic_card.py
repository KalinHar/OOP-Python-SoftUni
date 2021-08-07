from project.card.magic_card import MagicCard
from unittest import TestCase, main


class TestMagicCard(TestCase):
    def setUp(self):
        self.mc = MagicCard("mag")

    def test_init_correct(self):
        self.assertEqual("mag", self.mc.name)
        self.assertEqual(5, self.mc.damage_points)
        self.assertEqual(80, self.mc.health_points)

    def test_incorrect_name(self):
        with self.assertRaises(Exception) as ex:
            self.mc.name = ""
        self.assertEqual("Card's name cannot be an empty string.",
                         str(ex.exception))

    def test_incorrect_damage(self):
        with self.assertRaises(Exception) as ex:
            self.mc.damage_points = -1
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_incorrect_health(self):
        with self.assertRaises(Exception) as ex:
            self.mc.health_points = -1
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))


if __name__ == "__main__":
    main()
