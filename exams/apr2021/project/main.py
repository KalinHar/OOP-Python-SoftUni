from exams.apr2021.project.controller import Controller
from exams.apr2021.project.fish.freshwater_fish import FreshwaterFish


def test_project():
    c = Controller()
    print(c.add_aquarium("FreshwaterAquarium", "River"))
    print(c.add_aquarium("SaltwaterAquarium", "Sea"))
    print(c.add_aquarium("SaltwaterAquarum", "Sea"))  # Msg invalid type
    print(c.add_decoration("Plant"))
    print(c.add_decoration("Plant"))
    print(c.add_decoration("Ornament"))
    print(c.add_decoration("Ornament"))
    print(c.add_decoration("Plan"))  # Msg invalid type
    print(c.decorations_repository.find_by_type("Plant"))  # object
    print("-------------------")
    print(c.insert_decoration("River", "Plant"))  # Success
    print(c.insert_decoration("River", "Ornament"))  # Success
    print(c.insert_decoration("Sea", "Ornament"))  # Success
    print(c.insert_decoration("Sea", "Plant"))  # Success
    print(c.insert_decoration("Sea", "Ornament"))  # Msg, no decor of type
    print(c.insert_decoration("Se", "Ornament"))  # None
    print("-------------------")
    print(c.add_fish("River", "FreshwaterFis", "notfish", 5, 10))  # msg no type fish
    print(c.add_fish("River", "FreshwaterFish", "ff1000", 5, 1000))  # success
    print(c.add_fish("River", "FreshwaterFish", "ff100", 5, 100))  # success
    print(c.add_fish("River", "FreshwaterFish", "ff10", 5, 10))  # success
    print(c.add_fish("River", "SaltwaterFish", "ff10", 5, 10))  # msg water not suit
    print(c.add_fish("Sea", "SaltwaterFish", "sf20", 5, 20))  # success
    print(c.add_fish("Sea", "SaltwaterFish", "sf200", 5, 200))  # success
    print(c.add_fish("Sea", "FreshwaterFish", "sf200", 5, 200))  # msg water not suit
    print(c.add_fish("Se", "FreshwaterFish", "sf200", 5, 200))  # None
    c.aquariums[1].capacity = 2
    print(c.add_fish("Sea", "SaltwaterFish", "sf200", 5, 200))  # msg not capacity
    print("-------------------")
    print(c.feed_fish("River"))  # 3
    print(c.feed_fish("Rive"))  # None
    print(c.feed_fish("Sea"))  # 2
    print("-------------------")
    print(c.calculate_value("Sea"))  # 220 + 15
    print(c.calculate_value("River"))  # 1110 + 15
    print(c.calculate_value("Se"))  # 0
    print("-------------------")
    ff1 = FreshwaterFish("ff1",5, 1)
    c.aquariums[0].add_fish(ff1)
    print(c.report())
    print("-------------------")
    c.aquariums[0].remove_fish(ff1)
    print(c.report())
    print("-------------------")

    # test raises - with incorrect strings and value
    # c.add_aquarium("FreshwaterAquarium", "")
    # c.add_fish("River", "FreshwaterFish", "", "Species", 20)
    # c.add_fish("River", "FreshwaterFish", "Name", "", 20)
    # c.add_fish("River", "FreshwaterFish", "Name", "Species", - 10)


if __name__ == '__main__':
    test_project()

# OUTPUT WITHOUT RAISES
# Successfully added FreshwaterAquarium.
# Successfully added SaltwaterAquarium.
# Invalid aquarium type.
# Successfully added Plant.
# Successfully added Plant.
# Successfully added Ornament.
# Successfully added Ornament.
# Invalid decoration type.
# <exams.apr2021.project.decoration.plant.Plant object at 0x01F61838>
# -------------------
# Successfully added Plant to River.
# Successfully added Ornament to River.
# Successfully added Ornament to Sea.
# Successfully added Plant to Sea.
# There isn't a decoration of type Ornament.
# None
# -------------------
# There isn't a fish of type FreshwaterFis.
# Successfully added FreshwaterFish to River.
# Successfully added FreshwaterFish to River.
# Successfully added FreshwaterFish to River.
# Water not suitable.
# Successfully added SaltwaterFish to Sea.
# Successfully added SaltwaterFish to Sea.
# Water not suitable.
# None
# Not enough capacity.
# -------------------
# Fish fed: 3
# None
# Fish fed: 2
# -------------------
# The value of Aquarium Sea is 235.00.
# The value of Aquarium River is 1125.00.
# The value of Aquarium Se is 0.00.
# -------------------
# River:
# Fish: ff1000 ff100 ff10 ff1
# Decorations: 2
# Comfort: 6
# Sea:
# Fish: sf20 sf200
# Decorations: 2
# Comfort: 6
# -------------------
# River:
# Fish: ff1000 ff100 ff10
# Decorations: 2
# Comfort: 6
# Sea:
# Fish: sf20 sf200
# Decorations: 2
# Comfort: 6
# -------------------