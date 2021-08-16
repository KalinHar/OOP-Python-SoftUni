import unittest

from project.controller import Controller
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class ControllerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def test_controller_is_properly_initialized(self):
        self.assertEqual(0, len(self.controller.player_repository.players))
        self.assertEqual(0, len(self.controller.card_repository.cards))

    def test_add_player_works_as_expected(self):
        m1 = self.controller.add_player('Beginner', 'Test1')
        m2 = self.controller.add_player('Advanced', 'Test2')
        self.assertEqual(2, len(self.controller.player_repository.players))
        p1 = self.controller.player_repository.players[0]
        p2 = self.controller.player_repository.players[1]
        self.assertEqual(True, isinstance(p1, Beginner))
        self.assertEqual(True, isinstance(p2, Advanced))
        self.assertEqual(
            'Successfully added player of type Beginner with username: Test1', m1)
        self.assertEqual(
            'Successfully added player of type Advanced with username: Test2', m2)

    def test_add_card_works_as_expected(self):
        expected_m1 = 'Successfully added card of type MagicCard with name: TestCard1'
        expected_m2 = 'Successfully added card of type TrapCard with name: TestCard2'
        m1 = self.controller.add_card('Magic', 'TestCard1')
        m2 = self.controller.add_card('Trap', 'TestCard2')
        self.assertEqual(2, len(self.controller.card_repository.cards))
        c1 = self.controller.card_repository.cards[0]
        c2 = self.controller.card_repository.cards[1]
        self.assertEqual(True, isinstance(c1, MagicCard))
        self.assertEqual(True, isinstance(c2, TrapCard))
        self.assertEqual(expected_m1, m1)
        self.assertEqual(expected_m2, m2)

    def test_add_player_card_works_as_expected(self):
        self.controller.add_player('Beginner', 'Test1')
        self.controller.add_card('Magic', 'TestCard1')
        m = self.controller.add_player_card('Test1', 'TestCard1')
        expected_m = 'Successfully added card: TestCard1 to user: Test1'
        self.assertEqual(expected_m, m)

    #
    def test_controller_when_fighting_p1_win_scenario(self):
        expected_m = 'Attack user health 345 - Enemy user health 0'
        self.controller.add_player('Beginner', 'Test1')
        self.controller.add_player('Advanced', 'Test2')

        for i in range(3):
            self.controller.add_card('Magic', f'MagicTestCard{i}')
            self.controller.add_player_card('Test1', f'MagicTestCard{i}')

        for i in range(3):
            self.controller.add_card('Trap', f'TrapTestCard{i}')
            self.controller.add_player_card('Test1', f'TrapTestCard{i}')

        m = self.controller.fight('Test1', 'Test2')
        self.assertEqual(expected_m, m)
    #
    # def test_controller_when_no_winner_scenario(self):
    #     expected_m = 'Attack user health 90 - Enemy user health 250'
    #     self.controller.add_player('Beginner', 'Test1')
    #     self.controller.add_player('Advanced', 'Test2')
    #
    #     m = self.controller.fight('Test1', 'Test2')
    #     self.assertEqual(expected_m, m)

    # def test_controller_when_player_not_found_scenario(self):
    #     expected_m = None
    #     self.controller.add_player('Beginner', 'Test1')
    #     self.controller.add_player('Advanced', 'Test2')
    #
    #     m = self.controller.fight('Test1', 'Test3')
    #     self.assertEqual(expected_m, m)

    # def test_controller_when_fighting_p2_win_scenario(self):
    #     expected_m = 'Attack user health 0 - Enemy user health 710'
    #     self.controller.add_player('Beginner', 'Test1')
    #     self.controller.add_player('Advanced', 'Test2')
    #
    #     for i in range(6):
    #         self.controller.add_card('Magic', f'MagicTestCard{i}')
    #         self.controller.add_player_card('Test2', f'MagicTestCard{i}')
    #
    #     for i in range(3):
    #         self.controller.add_card('Trap', f'TrapTestCard{i}')
    #         self.controller.add_player_card('Test2', f'TrapTestCard{i}')
    #
    #     self.controller.add_card('Magic', 'MagicTestCard')
    #     self.controller.add_player_card('Test1', 'MagicTestCard')
    #     m = self.controller.fight('Test1', 'Test2')
    #     self.assertEqual(expected_m, m)

    # def test_controller_report_gives_correct_details(self):
    #     self.controller.add_player('Beginner', 'Test1')
    #     self.controller.add_player('Advanced', 'Test2')
    #     self.controller.add_card('Magic', 'TestCard1')
    #     self.controller.add_card('Trap', 'TestCard2')
    #
    #     self.controller.add_card('Magic', 'MagicTestCard')
    #     self.controller.add_player_card('Test1', 'MagicTestCard')
    #
    #     for i in range(3):
    #         self.controller.add_card('Magic', f'MagicTestCard{i}')
    #         self.controller.add_player_card('Test1', f'MagicTestCard{i}')
    #
    #     for i in range(2):
    #         self.controller.add_card('Trap', f'TrapTestCard{i}')
    #         self.controller.add_player_card('Test2', f'TrapTestCard{i}')
    #
    #     expected_message = 'Username: Test1 - Health: 50 - Cards 4\n### Card: MagicTestCard - Damage: 5\n### Card: MagicTestCard0 - Damage: 5\n### Card: MagicTestCard1 - Damage: 5\n### Card: MagicTestCard2 - Damage: 5\nUsername: Test2 - Health: 250 - Cards 2\n### Card: TrapTestCard0 - Damage: 120\n### Card: TrapTestCard1 - Damage: 120'
    #     message = self.controller.report()
    #     self.assertEqual(expected_message, message)


if __name__ == "__main__":
    unittest.main()
