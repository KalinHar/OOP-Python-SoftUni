from workshop.fig_games.project.figure.figure import Figure
from math import pi as constant_Pi


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return self.radius * self.radius * constant_Pi

    def calculate_circumference(self):
        return self.radius * constant_Pi * 2


# f = Circle("ci1", 2)
# print(f.calculate_area())
# print(f.calculate_circumference())
# print(f.calculate_relativity)
