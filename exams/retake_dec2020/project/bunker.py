from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @staticmethod
    def get_objects(objects, obj_type):
        return [obj for obj in objects if isinstance(obj, obj_type)]

    @property
    def food(self):
        objects = self.get_objects(self.supplies, FoodSupply)
        if not objects:
            raise IndexError("There are no food supplies left!")
        return objects

    @property
    def water(self):
        objects = self.get_objects(self.supplies, WaterSupply)
        if not objects:
            raise IndexError("There are no water supplies left!")
        return objects

    @property
    def painkillers(self):
        objects = self.get_objects(self.medicine, Painkiller)
        if not objects:
            raise IndexError("There are no painkillers left!")
        return objects

    @property
    def salves(self):
        objects = self.get_objects(self.medicine, Salve)
        if not objects:
            raise IndexError("There are no salves left!")
        return objects

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.family_name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            med = self.painkillers[-1] if medicine_type == "Painkiller" else self.salves[-1]
            med.apply(survivor)
            self.medicine.remove(med)
            return f"{survivor.family_name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            sust = next(filter(lambda x: x.__class__.__name__ == sustenance_type, reversed(self.supplies)))
            sust.apply(survivor)
            self.supplies.remove(sust)
            return f"{survivor.family_name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for sur in self.survivors:
            sur.needs -= sur.age * 2
            self.sustain(sur,"FoodSupply")
            self.sustain(sur,"WaterSupply")
