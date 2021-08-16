import unittest

from project.card.magic_card import MagicCard
from project.player.advanced import Advanced


class AdvancedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Advanced('TestPlayer')

    def test_beginner_has_correct_attr_after_init(self):
        username = 'TestPlayer'
        hp = 250
        self.assertEqual(username, self.player.username)
        self.assertEqual(hp, self.player.health)
        self.assertEqual('CardRepository',
                         self.player.card_repository.__class__.__name__)

    def test_beginner_raises_when_empty_username(self):
        with self.assertRaises(ValueError) as context:
            self.player.username = ''
        msg = "Player's username cannot be an empty string."
        self.assertEqual(msg, str(context.exception))

    def test_beginner_raises_when_negative_hp(self):
        with self.assertRaises(ValueError) as context:
            self.player.health = -5
        msg = "Player's health bonus cannot be less than zero."
        self.assertEqual(msg, str(context.exception))

    def test_beginner_takes_damage_points(self):
        self.player.take_damage(5)
        self.assertEqual(245, self.player.health)

    def test_beginner_raises_when_negative_damage_points(self):
        with self.assertRaises(ValueError) as context:
            self.player.take_damage(-5)
        msg = "Damage points cannot be less than zero."
        self.assertEqual(msg, str(context.exception))

    def test_beginner_is_dead_after_health_is_zero(self):
        self.player.take_damage(250)
        self.assertEqual(True, self.player.is_dead)

    def test_beginner_is_dead_after_health_is_negative(self):
        self.player.take_damage(250)
        self.assertEqual(True, self.player.is_dead)

    def test_apply_regular_bonus_works_correctly(self):
        card = MagicCard('Test')
        self.player.card_repository.add(card)
        self.player.apply_bonus()
        self.assertEqual(330, self.player.health)
        self.assertEqual(5, card.damage_points)

    def test_advanced_has_correct_str_representation(self):
        card = MagicCard('Test')
        self.player.card_repository.add(card)
        expected_message = '\n'.join([
            'Username: TestPlayer - Health: 250 - Cards 1',
            '### Card: Test - Damage: 5'])
        self.assertEqual(expected_message, str(self.player))


if __name__ == "__main__":
    unittest.main()
