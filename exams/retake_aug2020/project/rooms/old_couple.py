from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, budget=pension_one+pension_two, members_count=2)
        self.room_cost = 15
        self.appliances = [Room.tv, Room.fr, Room.st] * self.members_count
        self.calculate_expenses(self.appliances)


# old = OldCouple("rety", 100, 100)
# print(old.expenses)