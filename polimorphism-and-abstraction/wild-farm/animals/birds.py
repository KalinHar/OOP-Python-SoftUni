from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    _food_types = (Meat, )
    _increase_with = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    # def feed(self, food):
    #     if type(food) == Meat:
    #         self.food_eaten += food.quantity
    #         self.weight += food.quantity * self._increase_with
    #         return
    #     return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    _food_types = (Vegetable, Fruit, Meat, Seed)
    _increase_with = 0.35

    def make_sound(self):
        return "Cluck"

    # def feed(self, food):
    #     if type(food) in (Vegetable, Fruit, Meat, Seed):
    #         self.food_eaten += food.quantity
    #         self.weight += food.quantity * self._increase_with
    #         return
    #     return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
    #
