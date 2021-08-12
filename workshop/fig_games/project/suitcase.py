from workshop.fig_games.project.figure.figure import Figure
from workshop.fig_games.project.figure.circle import Circle
from workshop.fig_games.project.figure.rectangle import Rectangle
from workshop.fig_games.project.figure.triangle import Triangle


class Suitcase:
    def __init__(self):
        self.repository = []

    def add(self, figure):
        if not isinstance(figure, Figure):
            raise TypeError("The type of Figure is incorrect!")
        if self.get_figure(figure.name):
            raise KeyError("Figure name already exist!")
        self.repository.append(figure)
        return f"Figure: {figure.name} added."

    def remove(self, figure_name):
        fig = self.get_figure(figure_name)
        if not fig:
            raise KeyError(f"Figure: {figure_name} not exist!")
        self.repository.remove(fig)
        return f"Figure: {figure_name} removed."

    def get_figure(self, figure_name):
        fig = next(filter(lambda f: f.name == figure_name, self.repository), None)
        return fig

    def __repr__(self):
        return ", ".join(f.name for f in self.repository)


# f = Circle("c5", 5)
# f1 = Circle("c6", 6)
# f2 = Triangle("tri1", 6, 2, 3, 4)
# f3 = Rectangle("rec1", 6, 5)
# f4 = Rectangle("rec2", 4, 1)
#
# case = Suitcase()
# case.add(f)
# case.add(f2)
# case.add(f3)
# case.add(f4)
# print(case.repository[0].name)
# case.add(f1)
# print(case.repository[1].name)
# case.remove("c5")
# print(repr(case))
# case.add("frt")
