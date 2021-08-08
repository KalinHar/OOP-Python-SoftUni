from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        if fish.__class__.__name__[:-4] == self.__class__.__name__[:-8]:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):
        result = [f"{self.name}:"]
        f_names = " ".join([f.name for f in self.fish]) if [f.name for f in self.fish] else "none"
        result.append(f"Fish: {f_names}")
        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {sum(d.comfort for d in self.decorations)}")
        return "\n".join(result)

