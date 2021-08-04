from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError()

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError()

    @abstractmethod
    def create_table(self):
        raise NotImplementedError()


class Chair:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Table:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Victorian Chair')

    def create_sofa(self):
        return Sofa('Victorian Sofa')

    def create_table(self):
        return Table('Victorian Table')


class BarokFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Barok Chair')

    def create_sofa(self):
        return Sofa('Barok Sofa')

    def create_table(self):
        return Table('Barok Table')


