from project.rooms.room import Room
from project.people.child import Child
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from unittest import TestCase, main


class TestRoom(TestCase):
    def setUp(self):
        self.room = Room("Family", 200, 2)

    def test_init(self):
        self.assertEqual("Family", self.room.family_name)
        self.assertEqual(200, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertListEqual([], self.room.children)
        self.assertEqual(self.room.expenses, 0)

    def test_calc_exp(self):
        child1 = Child(5, 1, 2, 1)
        child2 = Child(3, 2)
        young_couple = YoungCoupleWithChildren("Johnsons", 150, 205, child1, child2)
        young_couple.calculate_expenses(young_couple.children, young_couple.appliances)
        self.assertEqual(864, young_couple.expenses)

    def test_exp_correct_setter(self):
        self.room.expenses = 100
        self.assertEqual(100, self.room.expenses)

    def test_exp_incorrect_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -20
        self.assertEqual("Expenses cannot be negative", str(ex.exception))


if __name__ == "__main__":
    main()