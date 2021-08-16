import unittest

from project.card.trap_card import TrapCard


class TrapCardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.card = TrapCard('TestCard')

    def test_card_has_correct_attr_after_init(self):
        name = 'TestCard'
        damage_points = 120
        health_points = 5
        self.assertEqual(
            (name, damage_points, health_points),
            (self.card.name, self.card.damage_points, self.card.health_points))

    def test_card_raises_when_empty_name(self):
        with self.assertRaises(ValueError) as ctx:
            self.card.name = ''
        msg = "Card's name cannot be an empty string."
        self.assertEqual(msg, str(ctx.exception))

    def test_card_raises_when_negative_damage_points(self):
        with self.assertRaises(ValueError) as ctx:
            self.card.damage_points = -5
        msg = "Card's damage points cannot be less than zero."
        self.assertEqual(msg, str(ctx.exception))

    def test_card_raises_when_negative_health_points(self):
        with self.assertRaises(ValueError) as ctx:
            self.card.health_points = -5
        msg = "Card's HP cannot be less than zero."
        self.assertEqual(msg, str(ctx.exception))

    def test_trap_card_has_correct_str_representation(self):
        expected_message = "### Card: TestCard - Damage: 120"
        self.assertEqual(expected_message, str(self.card))


if __name__ == "__main__":
    unittest.main()
