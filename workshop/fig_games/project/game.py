from workshop.fig_games.project.suitcase import Suitcase
from workshop.fig_games.project.battle.area_battle import AreaBattle
from workshop.fig_games.project.battle.circumfernce_battle import CircumferenceBattle
from workshop.fig_games.project.battle.relative_battle import RelativeBattle
from workshop.fig_games.project.figure.triangle import Triangle
from workshop.fig_games.project.figure.circle import Circle
from workshop.fig_games.project.figure.square import Square
from workshop.fig_games.project.figure.rectangle import Rectangle


class Game:
    def __init__(self):
        self.figures = Suitcase()

    def area_battle(self, fig1, fig2):
        result = AreaBattle().battle(fig1, fig2)
        if result:
            return result.name
        return None

    def circumference_battle(self, fig1, fig2):
        result = CircumferenceBattle().battle(fig1, fig2)
        if result:
            return result.name
        return None

    def relative_battle(self, fig1, fig2):
        result = RelativeBattle().battle(fig1, fig2)
        if result:
            return result.name
        return None

    def total_battle(self):
        while len(self.figures.repository) > 1:
            fig1 = self.figures.repository.pop()  # take first two figs
            fig2 = self.figures.repository.pop()  # take first two figs
            result = [self.area_battle(fig1, fig2)]
            result.append(self.circumference_battle(fig1, fig2))
            result = [fig for fig in result if fig]  # list with only wins results
            result = set(result)
            result = list(result)
            if len(result) == 1:  # check for winner
                self.figures.add([f for f in [fig1, fig2] if f.name == result[0]][0])  # return the winner back
                continue
            result = self.relative_battle(fig1, fig2)
            self.figures.add([f for f in (fig1, fig2) if f.name == result][0])  # return the winner back
        return self.figures.repository[0]

    def __str__(self):
        return f"The winner is:\n{str(self.total_battle())}"


tri1 = Triangle("tri1", 9, 4, 6.5, 4.5)
tri2 = Triangle("tri2", 5, 2.4, 3, 4)
cir1 = Circle("cir1", 3)
rec1 = Rectangle("rec1", 1, 7)
squ1 = Square("squ1", 6)
g = Game()
print(g.figures.add(tri1))
print(g.figures.add(tri2))
print(g.figures.add(cir1))
print(g.figures.add(rec1))
print(g.figures.add(squ1))
print(g.area_battle(cir1, tri1))
print(g.circumference_battle(cir1, tri1))
print(g.relative_battle(cir1, tri1))
print(g.figures.remove("squ1"))
print(g.figures)
print("-------------")
print(g)