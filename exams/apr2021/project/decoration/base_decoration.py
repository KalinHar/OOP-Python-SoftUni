from abc import ABC, abstractmethod


class BaseDecoration:
    @abstractmethod
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price
