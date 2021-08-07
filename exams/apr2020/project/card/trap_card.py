from project.card.card import Card


class TrapCard(Card):
    def __init__(self, name):
        super().__init__(name, 120, 5)


# tr = TrapCard("trap")
# print(tr.damage_points)
# print(tr.health_points)
# tr.health_points = -2
