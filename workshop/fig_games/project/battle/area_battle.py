from workshop.fig_games.project.battle.battle import Battle


class AreaBattle(Battle):
    def battle(self, fig1, fig2):
        if fig1.calculate_area() > fig2.calculate_area():
            return fig1
        elif fig1.calculate_area() < fig2.calculate_area():
            return fig2
        return None
