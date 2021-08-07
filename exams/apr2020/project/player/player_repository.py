class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        if player.username in [p.username for p in self.players]:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        self.players = [p for p in self.players if p.username != player]
        self.count -= 1

    def find(self, username):
        return next(filter(lambda p: p.username == username, self.players), None)
