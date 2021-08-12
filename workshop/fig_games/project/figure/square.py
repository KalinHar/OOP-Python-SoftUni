from workshop.fig_games.project.figure.figure import Figure


class Square(Figure):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def calculate_circumference(self):
        return self.side * 4


# f = Square("sq1", 4)
# print(f.calculate_area())
# print(f.calculate_circumference())
# print(f.calculate_relativity)
# print(f)
