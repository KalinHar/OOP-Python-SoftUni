from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name=name, species=species, size=5, price=price)

    def eat(self):
        self.size += 2


# swf = SaltwaterFish("nam", "tr", 100)
# swf.eat()
# swf.eat()
# swf.eat()
# print(swf.__dict__)
