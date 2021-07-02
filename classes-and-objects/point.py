class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, param):
        self.x = param

    def set_y(self, param):
        self.y = param

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
