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


# c = Controller()
# print(c.add_aquarium("FreshwaterAquarium", "River"))
# print(c.add_aquarium("SaltwaterAquarium", "Sea"))
# print(c.add_aquarium("SaltwaterAquarum", "Sea"))  # Msg invalid type
# print(c.add_decoration("Plant"))
# print(c.add_decoration("Plant"))
# print(c.add_decoration("Ornament"))
# print(c.add_decoration("Ornament"))
# print(c.add_decoration("Plan"))  # Msg invalid type
# print(c.decorations_repository.find_by_type("Plant"))  # object
# print("-------------------")
# print(c.insert_decoration("River", "Plant"))  # Success
# print(c.insert_decoration("River", "Ornament"))  # Success
# print(c.insert_decoration("Sea", "Ornament"))  # Success
# print(c.insert_decoration("Sea", "Plant"))  # Success
# print(c.insert_decoration("Sea", "Ornament"))  # Msg, no decor of type
# print(c.insert_decoration("Se", "Ornament"))  # None
# print("-------------------")
# print(c.add_fish("River", "FreshwaterFis", "notfish", 5, 10))  # msg no type fish
# print(c.add_fish("River", "FreshwaterFish", "ff1000", 5, 1000))  # success
# print(c.add_fish("River", "FreshwaterFish", "ff100", 5, 100))  # success
# print(c.add_fish("River", "FreshwaterFish", "ff10", 5, 10))  # success
# print(c.add_fish("River", "SaltwaterFish", "ff10", 5, 10))  # msg water not suit
# print(c.add_fish("Sea", "SaltwaterFish", "sf20", 5, 20))  # success
# print(c.add_fish("Sea", "SaltwaterFish", "sf200", 5, 200))  # success
# print(c.add_fish("Sea", "FreshwaterFish", "sf200", 5, 200))  # msg water not suit
# print(c.add_fish("Se", "FreshwaterFish", "sf200", 5, 200))  # None
# c.aquariums[1].capacity = 2
# print(c.add_fish("Sea", "SaltwaterFish", "sf200", 5, 200))  # msg not capacity
# print("-------------------")
# print(c.feed_fish("River"))  # 3
# print(c.feed_fish("Rive"))  # None
# print(c.feed_fish("Sea"))  # 2
# print("-------------------")
# print(c.calculate_value("Sea"))  # 220 + 15
# print(c.calculate_value("River"))  # 1110 + 15
# print(c.calculate_value("Se"))  # 0
# print("-------------------")
# ff1 = FreshwaterFish("ff1",5, 1)
# c.aquariums[0].add_fish(ff1)
# print(c.report())
# print("-------------------")
# c.aquariums[0].remove_fish(ff1)
# print(c.report())
# print("-------------------")
# test with incorrect strings and value
# c.add_aquarium("FreshwaterAquarium", "")
# c.add_fish("River", "FreshwaterFish", "", "Species", 20)
# c.add_fish("River", "FreshwaterFish", "Name", "", 20)
# c.add_fish("River", "FreshwaterFish", "Name", "Species", - 10)
