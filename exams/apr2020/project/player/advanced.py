from project.player.player import Player


class Advanced(Player):
    def __init__(self, username):
        super().__init__(username, 250)


# ad = Advanced("Advance")
# ad.take_damage(50)
# print(ad.health)
# print(ad.is_dead)
