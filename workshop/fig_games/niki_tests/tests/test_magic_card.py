import unittest

from project.card.magic_card import MagicCard


class MagicCardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.card = MagicCard('TestCard')

    def test_card_has_correct_attr_after_init(self):
        name = 'TestCard'
        damage_points = 5
        health_points = 80
        self.assertEqual(name, self.card.name)
        self.assertEqual(damage_points, self.card.damage_points)
        self.assertEqual(health_points, self.card.health_points)

    def test_card_raises_when_empty_name(self):
        with self.assertRaises(ValueError) as context:
            self.card.name = ''
        msg = "Card's name cannot be an empty string."
        self.assertEqual(msg, str(context.exception))

    def test_card_raises_when_negative_damage_points(self):
        with self.assertRaises(ValueError) as context:
            self.card.damage_points = -5
        msg = "Card's damage points cannot be less than zero."
        self.assertEqual(msg, str(context.exception))

    def test_card_raises_when_negative_health_points(self):
        with self.assertRaises(ValueError) as context:
            self.card.health_points = -5
        msg = "Card's HP cannot be less than zero."
        self.assertEqual(msg, str(context.exception))

    def test_magic_card_has_correct_str_representation(self):
        expected_message = "### Card: TestCard - Damage: 5"
        self.assertEqual(expected_message, str(self.card))


if __name__ == "__main__":
    unittest.main()
