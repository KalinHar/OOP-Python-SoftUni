from workshop.fig_games.project.figure.figure import Figure


class Triangle(Figure):
    def __init__(self, name, side_a, height_a, side_b, side_c):
        super().__init__(name)
        self.side_a = side_a
        self.height_a = height_a
        self.side_b = side_b
        self.side_c = side_c

    def calculate_area(self):
        return self.side_a * self.height_a / 2

    def calculate_circumference(self):
        return self.side_a + self.side_b + self.side_c


# f = Triangle("tri1", 9, 4, 6.5, 4.5)
# print(f.name)
# print(f.calculate_area())
# print(f.calculate_circumference())
# print(f.calculate_relativity)
# print(f)