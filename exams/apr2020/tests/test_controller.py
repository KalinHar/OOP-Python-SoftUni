from project.controller import Controller
from project.battle_field import BattleField
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.trap_card import TrapCard
from project.card.magic_card import MagicCard
from unittest import TestCase, main


class TestController(TestCase):
    def setUp(self):
        self.c = Controller()
        self.cm = MagicCard("mag")
        self.ct = TrapCard("tra")
        self.adv = Advanced("adv")
        self.beg = Beginner("beg")

    def test_init(self):
        self.assertEqual("PlayerRepository", self.c.player_repository.__class__.__name__)
        self.assertEqual("CardRepository", self.c.card_repository.__class__.__name__)

    def test_add_player(self):
        self.assertEqual("Successfully added player of type Beginner with username: beg", self.c.add_player("Beginner", "beg"))
        self.assertEqual("Successfully added player of type Advanced with username: adv", self.c.add_player("Advanced", "adv"))
        self.assertEqual(2, self.c.player_repository.count)
        self.assertTrue(isinstance(self.c.player_repository.players[0], Beginner))
        self.assertEqual("beg", self.c.player_repository.players[0].username)
        self.assertTrue(isinstance(self.c.player_repository.players[1], Advanced))
        self.assertEqual("adv", self.c.player_repository.players[1].username)

    def test_add_card(self):
        self.assertEqual('Successfully added card of type MagicCard with name: mag', self.c.add_card("Magic", "mag"))
        self.assertEqual('Successfully added card of type TrapCard with name: tra', self.c.add_card("Trap", "tra"))
        self.assertEqual(2, self.c.card_repository.count)
        self.assertTrue(isinstance(self.c.card_repository.cards[0], MagicCard))
        self.assertEqual("mag", self.c.card_repository.cards[0].name)
        self.assertTrue(isinstance(self.c.card_repository.cards[1], TrapCard))
        self.assertEqual("tra", self.c.card_repository.cards[1].name)

    def test_add_player_card(self):
        self.c.add_player("Beginner", "beg")
        self.c.add_card("Magic", "mag")
        self.assertEqual("Successfully added card: mag to user: beg",
                         self.c.add_player_card("beg", "mag"))
        self.assertEqual("mag", self.c.player_repository.players[0].card_repository.cards[0].name)

    def test_fight(self):
        self.c.add_player("Advanced", "adv")
        self.c.add_player("Beginner", "beg")
        self.c.add_card("Magic", "mag")
        self.c.add_card("Trap", "tra")
        self.c.add_player_card("adv", "mag")
        self.c.add_player_card("beg", "tra")
        self.assertEqual("Attack user health 180 - Enemy user health 90",
                         self.c.fight("adv", "beg"))

    # def test_controller_when_fighting_p1_win_scenario(self):
    #     expected_m = 'Attack user health 345 - Enemy user health 0'
    #     self.c.add_player('Beginner', 'Test1')
    #     self.c.add_player('Advanced', 'Test2')
    #
    #     for i in range(3):
    #         self.c.add_card('Magic', f'MagicTestCard{i}')
    #         self.c.add_player_card('Test1', f'MagicTestCard{i}')
    #
    #     for i in range(3):
    #         self.c.add_card('Trap', f'TrapTestCard{i}')
    #         self.c.add_player_card('Test1', f'TrapTestCard{i}')
    #
    #     m = self.c.fight('Test1', 'Test2')
    #     self.assertEqual(expected_m, m)

    def test_report(self):
        self.c.add_player("Advanced", "adv")
        self.c.add_player("Beginner", "beg")
        self.c.add_card("Magic", "mag")
        self.c.add_card("Trap", "tra")
        self.c.add_player_card("adv", "mag")
        self.c.add_player_card("beg", "tra")
        self.assertEqual("Username: adv - Health: 250 - Cards 1\n"
                         "### Card: mag - Damage: 5\n"
                         "Username: beg - Health: 50 - Cards 1\n"
                         "### Card: tra - Damage: 120\n",
                         self.c.report())
    #
    # def test_controller_when_player_not_found_scenario(self):
    #     expected_m = None
    #     self.c.add_player('Beginner', 'Test1')
    #     self.c.add_player('Advanced', 'Test2')
    #
    #     m = self.c.fight('Test1', 'Test3')
    #     self.assertEqual(expected_m, m)


if __name__ == "__main__":
     main()
