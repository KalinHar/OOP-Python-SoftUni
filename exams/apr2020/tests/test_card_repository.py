from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from unittest import TestCase, main


class TestCardRepository(TestCase):
    def setUp(self):
        self.cr = CardRepository()

    def test_init(self):
        self.assertEqual(0, self.cr.count)
        self.assertEqual([], self.cr.cards)

    def test_add_correct(self):
        card = MagicCard('mag')
        self.cr.add(card)
        self.assertEqual(1, self.cr.count)
        self.assertEqual([card], self.cr.cards)

    def test_add_incorrect(self):
        card = MagicCard('mag')
        self.cr.add(card)
        with self.assertRaises(Exception) as ex:
            self.cr.add(card)
        self.assertEqual("Card mag already exists!", str(ex.exception))

    def test_remove_correct(self):
        card = MagicCard('mag')
        self.cr.cards = [card]
        self.cr.count = 1
        self.cr.remove("mag")
        self.assertEqual(0, self.cr.count)
        self.assertEqual([], self.cr.cards)

    def test_remove_incorrect(self):
        with self.assertRaises(Exception) as ex:
            self.cr.remove("")
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))
        self.assertEqual(0, self.cr.count)
        self.assertEqual([], self.cr.cards)

    def test_find(self):
        card = MagicCard('mag')
        self.cr.add(card)
        self.assertEqual(card, self.cr.find('mag'))


if __name__ == "__main__":
    main()
