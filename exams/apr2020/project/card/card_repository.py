class CardRepository:
    def __init__(self):
        self.cards = []
        self.count = 0

    def add(self, card):
        if card.name in [c.name for c in self.cards]:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        self.cards = [c for c in self.cards if c.name != card]
        self.count -= 1

    def find(self, name):
        return next(filter(lambda c: c.name == name, self.cards), None)