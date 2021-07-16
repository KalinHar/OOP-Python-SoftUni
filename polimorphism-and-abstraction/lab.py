from abc import ABC, abstractmethod

class Shape:
    def calculate_area(self):
        return None


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


for obj in Square(), Triangle():
    print(obj.calculate_area())
#----------------------------------------------------
# for obj in Square(), Triangle():
#     if type(obj).__name__ == "Square":
#         area = obj.calculate_square_area()
#     elif type(obj).__name__ == "Triangle":
#         area = obj.calculate_triangle_area()
#     print(area)
#----------------------------------------------------


class MyClass:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __len__(self):
        return self.size


my_class = MyClass("Class Name", 3)
print(len(my_class)) # 3


class Purchase:
    def __init__(self, product_name, cost):
        self.product_name = product_name
        self.cost = cost

    def __add__(self, other):
        return self.cost + other.cost


first_purchase = Purchase('sofa', 650)
second_purchase = Purchase('table', 150)
print(first_purchase + second_purchase)  # 800
print(first_purchase.__add__(second_purchase))  # 800
print(first_purchase.cost + second_purchase.cost)  # 800


class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


person_one = Person('John', 20)
person_two = Person('Natasha', 36)
print(person_one > person_two)  # False
print(person_one.salary > person_two.salary)  # False
print(person_one.salary > 10)  # True

# duck typing ---------------------------------------
# we don't care of object, only same method
class Cat:
    def sound(self):
        print("Meow!")


class Train:
    def sound(self):
        print("Sound from wheels slipping!")


for any_type in Cat(), Train():
    any_type.sound()

#---------------------------------------------------------


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        raise NotImplementedError("Subclass must implement")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Meow!")


cat = Cat("Willy")
cat.sound()
dog = Dog("Willy")
dog.sound()
animal = Animal("Willy")
animal.sound()  # NotImplementedError
