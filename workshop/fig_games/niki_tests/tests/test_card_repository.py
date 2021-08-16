import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class cardRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.magic_card = MagicCard('Magic')
        self.trap_card = TrapCard('Trap')
        self.pr = CardRepository()

    def test_card_repository_has_correct_attr_when_initialized(self):
        self.assertEqual([], self.pr.cards)
        self.assertEqual(0, self.pr.count)

    def test_card_repository_can_add_single_card(self):
        self.pr.add(self.magic_card)
        self.assertEqual(1, len(self.pr.cards))
        self.assertEqual(1, self.pr.count)
        self.assertIn(self.magic_card, self.pr.cards)

    def test_card_repository_can_add_multiple_cards(self):
        self.pr.add(self.magic_card)
        self.pr.add(self.trap_card)
        self.assertEqual(2, len(self.pr.cards))
        self.assertEqual(2, self.pr.count)
        self.assertIn(self.magic_card, self.pr.cards)
        self.assertIn(self.trap_card, self.pr.cards)

    def test_card_repository_raises_when_adding_same_card_twice(self):
        self.pr.add(self.magic_card)
        with self.assertRaises(ValueError) as ctx:
            self.pr.add(self.magic_card)
        msg = "Card Magic already exists!"
        self.assertEqual(msg, str(ctx.exception))

    def test_card_repository_removes_card_correctly(self):
        self.pr.add(self.magic_card)
        self.pr.add(self.trap_card)
        self.assertIn(self.magic_card, self.pr.cards)
        self.assertIn(self.trap_card, self.pr.cards)
        self.pr.remove('Magic')
        self.assertEqual(1, self.pr.count)
        self.assertIn(self.trap_card, self.pr.cards)
        self.assertNotIn(self.magic_card, self.pr.cards)

    def test_card_repository_raises_when_removing_empty_name(self):
        self.pr.add(self.magic_card)
        with self.assertRaises(ValueError) as context:
            self.pr.remove('')
        msg = "Card cannot be an empty string!"
        self.assertEqual(msg, str(context.exception))

    def test_card_repository_does_nothing_when_removing_non_present_card(self):
        self.pr.add(self.magic_card)
        self.pr.remove('Trap')
        self.assertEqual(1, self.pr.count)

    def test_user_repository_finds_correct_card(self):
        self.pr.add(self.magic_card)
        self.pr.add(self.trap_card)
        p = self.pr.find('Magic')
        self.assertEqual(p, self.magic_card)

    def test_user_repository_find_gives_none_when_search_unsuccessful(self):
        self.pr.add(self.trap_card)
        p = self.pr.find('Magic')
        self.assertEqual(p, None)


if __name__ == "__main__":
    unittest.main()
