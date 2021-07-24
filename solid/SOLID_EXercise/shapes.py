from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


class Triangle(Shape):
    def __init__(self, *side):
        if len(side) == 2:
            self.side_a = side[0]
            self.h_a = side[1]
        else:
            self.side_a = side[0]
            self.side_b = side[1]
            self.side_c = side[2]

    def calculate_area(self):
        return (self.side_a * self.h_a)/2

    def calculate_perimeter(self):
        return self.side_c + self.side_b + self.side_a


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def calculate_area(self):
        return self.pi * self.radius * self.radius

    def calculate_perimeter(self):
        return self.pi * self.radius * 2


class Calculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise TypeError("Should be of type list")
        res = [shape for shape in value if not isinstance(shape, Shape)]
        if res:
            raise TypeError("All elements must be of type Shape")
        self.__shapes = value

    def add_shape(self, shape):
        if not isinstance(shape, Shape):
            raise TypeError("The element must be of type Shape")
        self.shapes.append(shape)


class PerimeterCalculator(Calculator):
    @property
    def total_perimeter(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_perimeter()
        return f"Total perimeter: {total}"

    @property
    def shapes_perimeters(self):
        total = ''
        for shape in self.shapes:
            total += f"{shape.__class__.__name__} : {shape.calculate_perimeter()}\n"
        return f"Shapes - perimeters:\n{total}"


class AreaCalculator(Calculator):
    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()
        return f"Total area: {total}"

    @property
    def shapes_areas(self):
        total = ''
        for shape in self.shapes:
            total += f"{shape.__class__.__name__} : {shape.calculate_area()}\n"
        return f"Shapes areas:\n{total}"


shapes_to_area = [Rectangle(1, 6), Triangle(2, 3), Circle(10)]
calc_area = AreaCalculator(shapes_to_area)
calc_area.add_shape(Triangle(100, 3))

calc_perim = PerimeterCalculator([Triangle(3, 4, 5), Circle(10)])

print(calc_area.total_area)
print(calc_area.shapes_areas)
print(calc_perim.shapes_perimeters)

calc_perim.add_shape(Rectangle(4, 5))
print(calc_perim.shapes_perimeters)


# TODO try to bring new feature Circle so that you follow OPen/closed principle
# shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(6)]
# calculator = AreaCalculator(shapes)


#TODO try to do it with mixins and check if there is not too much abstraction -
# try to make mro which will lead to the Diamond of the death problem - very common in multiple inheritance behaviour