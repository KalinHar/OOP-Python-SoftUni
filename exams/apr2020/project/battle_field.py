from project.player.beginner import Beginner


class BattleField:
    @staticmethod
    def fight(attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        for pl in (attacker, enemy):
            if isinstance(pl, Beginner):
                pl.health += 40
                for c in pl.card_repository.cards:
                    c.damage_points += 30

        for pl in (attacker, enemy):
            pl.health += sum(c.health_points for c in pl.card_repository.cards)

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
