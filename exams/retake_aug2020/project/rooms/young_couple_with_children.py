from project.rooms.room import Room
from project.people.child import Child


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, budget=salary_one+salary_two, members_count=2+len(children))
        self.room_cost = 30
        self.appliances = [Room.tv, Room.fr, Room.la] * self.members_count
        self.children = list(children)
        self.calculate_expenses(self.children, self.appliances)


# child1 = Child(5, 1, 2, 1)
# child2 = Child(3, 2)
# young_couple = YoungCoupleWithChildren("Johnsons", 150, 205, child1, child2)
# print(young_couple.expenses)
