from exams.aug2021.project.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, 2.50, brand)


# t = Tea("lem", 200, "ET")
# print(t.name, t.portion, t.price, t.brand)
