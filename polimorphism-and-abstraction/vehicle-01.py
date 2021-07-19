from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_condition_consumption = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if distance * (self.fuel_consumption + Car.air_condition_consumption) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + Car.air_condition_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_condition_consumption = 1.6
    tiny_hole = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if distance * (self.fuel_consumption + Truck.air_condition_consumption) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + Truck.air_condition_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.tiny_hole


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
