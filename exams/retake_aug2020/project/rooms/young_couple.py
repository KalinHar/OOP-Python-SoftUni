from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, budget=salary_one+salary_two, members_count=2)
        self.room_cost = 20
        self.appliances = [Room.tv, Room.fr, Room.la] * self.members_count
        self.calculate_expenses(self.appliances)
