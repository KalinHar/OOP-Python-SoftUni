from exams.apr2021.project.aquarium.freshwater_aquarium import FreshwaterAquarium
from exams.apr2021.project.aquarium.saltwater_aquarium import SaltwaterAquarium
from exams.apr2021.project.decoration.decoration_repository import DecorationRepository
from exams.apr2021.project.decoration.ornament import Ornament
from exams.apr2021.project.decoration.plant import Plant
from exams.apr2021.project.fish.freshwater_fish import FreshwaterFish
from exams.apr2021.project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."
        aqua = FreshwaterAquarium(aquarium_name) if aquarium_type == "FreshwaterAquarium"\
            else SaltwaterAquarium(aquarium_name)
        self.aquariums.append(aqua)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."
        decor = Ornament() if decoration_type == "Ornament" else Plant()
        self.decorations_repository.add(decor)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        list_aq =[a for a in self.aquariums if a.name == aquarium_name]
        if list_aq:
            decor = self.decorations_repository.find_by_type(decoration_type)
            if decor == "None":
                return f"There isn't a decoration of type {decoration_type}."
            list_aq[0].add_decoration(decor)
            self.decorations_repository.remove(decor)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        fish = FreshwaterFish(fish_name, fish_species, price) if fish_type == "FreshwaterFish"\
            else SaltwaterFish(fish_name, fish_species, price)
        list_aq = [a for a in self.aquariums if a.name == aquarium_name]
        if list_aq:
            msg = list_aq[0].add_fish(fish)
            if not msg:
                return "Water not suitable."
            return msg

    def feed_fish(self, aquarium_name):
        list_aq = [a for a in self.aquariums if a.name == aquarium_name]
        if list_aq:
            list_aq[0].feed()
            return f"Fish fed: {len(list_aq[0].fish)}"

    def calculate_value(self, aquarium_name):
        list_aq = [a for a in self.aquariums if a.name == aquarium_name]
        value = 0
        if list_aq:
            fish_pr = sum(f.price for f in list_aq[0].fish)
            dec_pr = sum(d.price for d in list_aq[0].decorations)
            value = fish_pr + dec_pr
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = []
        for aqua in self.aquariums:
            result.append(str(aqua))
        return "\n".join(result)


