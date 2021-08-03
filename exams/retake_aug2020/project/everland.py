class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def total_consumption(self):
        return sum(r.expenses + r.room_cost for r in self.rooms)

    def get_monthly_consumptions(self):
        return f"Monthly consumptions: {self.total_consumption():.2f}$."

    def pay(self):
        unpaid_rooms = []
        result = []
        for r in self.rooms:
            if r.budget >= r.expenses + r.room_cost:
                r.budget -= r.expenses + r.room_cost
                result.append(f"{r.family_name} paid {r.expenses + r.room_cost:.2f}$ and have {r.budget:.2f}$ left.")
            else:
                result.append(f"{r.family_name} does not have enough budget and must leave the hotel.")
                unpaid_rooms.append(r)
        self.rooms = [r for r in self.rooms if r not in unpaid_rooms]
        return "\n".join(result)

    def status(self):
        result = [f"Total population: {sum(r.members_count for r in self.rooms)}"]
        for r in self.rooms:
            result.append(f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$")
            for n, ch in enumerate(r.children):
                result.append(f"--- Child {n+1} monthly cost: {ch.cost * 30:.2f}$")
            result.append(f"--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in r.appliances):.2f}$")
        return "\n".join(result)
