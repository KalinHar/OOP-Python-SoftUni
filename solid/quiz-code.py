# Example 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError
        self.__age = value

    def greet(self):
        return "Hello, I am a human"


# Example 2
class Employee(Person):
    min_age = 16
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def validate_age(value):
        if value < Employee.min_age or \
           value > Employee.max_age:
            raise ValueError()

    def show_min_age(self):
        return self.min_age


# Example 3

class GreetsMixin:
    def greet(self):
        return "Hello!"


class Manager(Person, GreetsMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


#Example 4

class Card:
    def __init__(self, holder_name):
        self.holder_name = holder_name
        self.__cvv = 5


# Example 5

class ExampleClass:
    my_class_attr = 6

    def __init__(self):
        self.my_instance_attr = 5

    @classmethod
    def get_instance_attr(cls):
        return cls.my_instance_attr



# Example 6
from abc import ABC
class Being(ABC):
    pass


# Example 7
class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
