from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.family_name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.family_name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.family_name} to the guild {self.name}"

    def kick_player(self, player_name):
        for pl in self.players:
            if pl.family_name == player_name:
                pl.guild = "Unaffiliated"
                self.players.remove(pl)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + "\n".join([pl.player_info() for pl in self.players])


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
