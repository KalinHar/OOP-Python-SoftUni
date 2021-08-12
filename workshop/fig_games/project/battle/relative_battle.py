from workshop.fig_games.project.battle.battle import Battle


class RelativeBattle(Battle):
    def battle(self, fig1, fig2):
        if fig1.relativity > fig2.relativity:
            return fig1
        elif fig1.relativity < fig2.relativity:
            return fig2
        return None
