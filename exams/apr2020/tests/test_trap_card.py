from project.card.trap_card import TrapCard
from unittest import TestCase, main


class TestTrapCard(TestCase):
    def setUp(self):
        self.mc = TrapCard("tra")

    def test_init_correct(self):
        self.assertEqual("tra", self.mc.name)
        self.assertEqual(120, self.mc.damage_points)
        self.assertEqual(5, self.mc.health_points)

    def test_init_incorrect_damage(self):
        with self.assertRaises(Exception) as ex:
            self.mc.damage_points = -1
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_init_incorrect_health(self):
        with self.assertRaises(Exception) as ex:
            self.mc.health_points = -1
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))


if __name__ == "__main__":
    main()
