# data_science_lect:1-3
# https://www.youtube.com/watch?v=JVFG9I_nHaA
# https://www.youtube.com/watch?v=wd2c-79zB6w
# https://www.youtube.com/watch?v=vALK84DEmsg

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = self.set_age(age)

    def change_name(self, new_name):
        self.name = new_name

    def set_age(self, age):
        if age <= 0:
            raise ValueError("Age must be positive")
        return age

    def __repr__(self):
        return "This is a person"


class Worker(Person):
    def __init__(self, name, age, date):
        super().__init__(name, age)
        # Person.__init__(self, name, age)
        self.date = date

    def __repr__(self):
        return super().__repr__() + " who is worker"


ww = Worker("rudi", 18, "june")
ww.change_name("fery")
print(ww.name)
print(ww)


