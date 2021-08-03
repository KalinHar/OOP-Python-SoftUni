class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.family_name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.family_name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.family_name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_for_salaries = sum([w.salary for w in self.workers])
        if sum_for_salaries <= self.__budget:
            self.__budget -= sum_for_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_for_tend = sum([a.money_for_care for a in self.animals])
        if sum_for_tend <= self.__budget:
            self.__budget -= sum_for_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]

        lions = [repr(a) for a in self.animals if a.__class__.__name__ == "Lion"]
        result.extend([f"----- {len(lions)} Lions:"])
        result.extend(lions)

        tigers = [repr(a) for a in self.animals if a.__class__.__name__ == "Tiger"]
        result.extend([f"----- {len(tigers)} Tigers:"])
        result.extend(tigers)

        cheetahs = [repr(a) for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result.extend([f"----- {len(cheetahs)} Cheetahs:"])
        result.extend(cheetahs)

        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]

        keepers = [a.__repr__() for a in self.workers if a.__class__.__name__ == "Keeper"]
        result.extend([f"----- {len(keepers)} Keepers:"])
        result.extend(keepers)

        caretakers = [a.__repr__() for a in self.workers if a.__class__.__name__ == "Caretaker"]
        result.extend([f"----- {len(caretakers)} Caretakers:"])
        result.extend(caretakers)

        vets = [a.__repr__() for a in self.workers if a.__class__.__name__ == "Vet"]
        result.extend([f"----- {len(vets)} Vets:"])
        result.extend(vets)

        return "\n".join(result)

