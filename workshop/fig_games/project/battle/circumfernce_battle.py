from workshop.fig_games.project.battle.battle import Battle


class CircumferenceBattle(Battle):
    def battle(self, fig1, fig2):
        if fig1.calculate_circumference() > fig2.calculate_circumference():
            return fig1
        elif fig1.calculate_circumference() < fig2.calculate_circumference():
            return fig2
        return None
