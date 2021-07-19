from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    _food_types = (Vegetable, Fruit)
    _increase_with = 0.10

    def make_sound(self):
        return "Squeak"

    # def feed(self, food):
    #     if type(food) in (Vegetable, Fruit):
    #         self.food_eaten += food.quantity
    #         self.weight += food.quantity * self._increase_with
    #         return
    #     return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    _food_types = (Meat, )
    _increase_with = 0.40

    def make_sound(self):
        return "Woof!"

    # def feed(self, food):
    #     if type(food) == Meat:
    #         self.food_eaten += food.quantity
    #         self.weight += food.quantity * self._increase_with
    #         return
    #     return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    _food_types = (Vegetable, Meat)
    _increase_with = 0.30

    def make_sound(self):
        return "Meow"

    # def feed(self, food):
    #     if type(food) in (Vegetable, Meat):
    #         self.food_eaten += food.quantity
    #         self.weight += food.quantity * self._increase_with
    #         return
    #     return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    _food_types = (Meat,)
    _increase_with = 1.00

    def make_sound(self):
        return "ROAR!!!"
    #
    # def feed(self, food):
    #     if type(food) == Meat:
    #         self.food_eaten += food.quantity
    #         self.weight += food.quantity * self._increase_with
    #         return
    #     return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
