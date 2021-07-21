from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        print("meow")


class Dog(Animal):
    def sound(self):
        print("bay")


animals = [Animal('cat'), Animal('dog')]
AdditionalSounds.animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи
# без да се налага да се правят промени по него
## при добавяне на нови животни
animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
