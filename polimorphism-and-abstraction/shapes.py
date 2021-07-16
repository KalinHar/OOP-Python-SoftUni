from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return self.__radius ** 2 * pi

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)


class Triangle(Shape):
    def __init__(self, height, *args):
        self.height = height
        self.sides = args

    def calculate_area(self):
        return self.sides[0] * self.height / 2

    def calculate_perimeter(self):
        return sum(self.sides)


triangle_a = Triangle(3, 4)
triangle_p = Triangle(0, 4, 5, 5)
print(triangle_a.calculate_area())
print(triangle_p.calculate_perimeter())

circle = Circle(5)
rectangle = Rectangle(10, 20)
triangle = Triangle(3, 4, 5, 5)
print("---------------")
for shape in circle, rectangle, triangle:
    print(shape.calculate_area())
    print(shape.calculate_perimeter())
    print("---------------")
