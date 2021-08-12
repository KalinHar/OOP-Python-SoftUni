from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_circumference(self):
        pass

    @property
    def relativity(self):
        return self.calculate_area() / self.calculate_circumference()

    def __str__(self):
        result = f"Figure name: {self.name}\n"\
                 f"Parameters: {', '.join(str(v) for k, v in self.__dict__.items() if k != 'name')}\n"\
                 f"Area: {self.calculate_area()}\n"\
                 f"Circumference: {self.calculate_circumference()}\n"\
                 f"Relativity: {self.relativity}"
        return result
