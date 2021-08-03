from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.laptop import Laptop


class Room:
    tv = TV()
    fr = Fridge()
    st = Stove()
    la = Laptop()

    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        self.expenses = sum(el.cost * 30 for arg in args for el in arg)
