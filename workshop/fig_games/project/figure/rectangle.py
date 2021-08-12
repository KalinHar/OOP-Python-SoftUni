from workshop.fig_games.project.figure.figure import Figure


class Rectangle(Figure):
    def __init__(self, name, side_a, side_b):
        super().__init__(name)
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self):
        return self.side_a * self.side_b

    def calculate_circumference(self):
        return (self.side_a + self.side_b) * 2


# f = Rectangle("rect1", 9, 4)
# print(f.name)
# print(f.calculate_area())
# print(f.calculate_circumference())
# print(f.calculate_relativity)
# print(f)
