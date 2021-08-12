from abc import ABC, abstractmethod


class Battle(ABC):
    @abstractmethod
    def battle(self, fig1, fig2):
        pass
