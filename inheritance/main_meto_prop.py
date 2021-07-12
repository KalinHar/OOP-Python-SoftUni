from dataclasses import dataclass


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


class Person2:
    def __init__(self, name):
        self._name = name

    name = property(
        lambda x: x._name,
        lambda x, value: x.__setattr__('_name', value),
        lambda x: x.__delattr__('_name'), 'Name property')


class Vacation:
    def __init__(self):
        self.is_on_vacation = False
        self.days_for_use = 0

    def set_vacation(self):
        self.is_on_vacation = not self.is_on_vacation

    def set_days_for_use(self, days):
        self.days_for_use = days


class Worker(Person, Vacation):
    def __init__(self, name, age, efficiency):
        super().__init__(name, age)
        # Person.__init__(self, name, age)
        Vacation.__init__(self)
        self.efficiency = efficiency

    def update_efficiency(self, new_effi):
        if self.efficiency < new_effi:
            self.efficiency = new_effi

    def __repr__(self):
        return super().__repr__() + " who is worker"


@dataclass
class Probs:
    """Docs for class Probs"""
    name: str
    age: int = 12


ww = Worker("Rudi", 18, "very good")
ww.change_name("Chery")
print(ww.name)
print(ww)
ww.set_vacation()
print(ww.is_on_vacation)
print(ww.__dict__)
print(repr(ww))
print("-----------------------------------------")
pepe = Probs("Pepe")
print(pepe)
print(pepe.name)
print(pepe.__doc__)

getattr(pepe, "name", "Error")  # error or None or anything, if no name
hasattr(pepe, "age")  # return True or False
setattr(pepe, "name", "George")  # change self.name to George or create it if not exist
delattr(pepe, "name")  # delete self.name

p2 = Person2('Dodror')
print(p2.__dict__)
print(hasattr(p2,"_name"))
print(hasattr(p2,"Dodror"))
