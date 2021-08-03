class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.family_name} has already joined"
        self.__players.append(player)
        return f"Player {player.family_name} joined team {self.__name}"

    def remove_player(self, player_name):
        for pl in self.__players:
            if pl.family_name == player_name:
                self.__players.remove(pl)
                return pl
        return f"Player {player_name} not found"
