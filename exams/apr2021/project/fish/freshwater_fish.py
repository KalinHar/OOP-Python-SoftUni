from exams.apr2021.project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name=name, species=species, size=3, price=price)

    def eat(self):
        self.size += 3


# fwf = FreshwaterFish("nam", "tr", 100)
# fwf.eat()
# fwf.eat()
# print(fwf.__dict__)
