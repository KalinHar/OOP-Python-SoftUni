class Area:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def surface_area(self):
        return f"{self.a * self.b:.2f}"


class Triangle(Area):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.b /= 2


class Rectangle(Area):
    def __init__(self, a, b):
        super().__init__(a, b)


class Square(Area):
    def __init__(self, a, b=None):
        super().__init__(a, b)
        self.b = self.a


class Circle(Area):
    def __init__(self, a, b=None):
        super().__init__(a, b)
        self.b = self.a * 3.14


tr = Triangle(3, 4)
sq = Square(4)
ci = Circle(10)
re = Rectangle(5, 4)
print(tr.surface_area())
print(sq.surface_area())
print(ci.surface_area())
print(re.surface_area())
