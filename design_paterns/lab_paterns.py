# https://refactoring.guru/design-patterns

def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper


@singleton
class DBConnection(object):
    def __init__(self):
        """Initialize your database connection here."""
        pass

    def __str__(self):
        return 'Database connection object'


# ---------------------------------------------
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class HtmlButton(Button):
    def __init__(self):
        pass

    def click(self):
        return f"{self.__class__.__name__}"


class WindowsButton(Button):
    def __init__(self):
        pass

    def click(self):
        return f"{self.__class__.__name__}"


os = "Web"


def get_button(os):
    if os == "Web":
        return HtmlButton()
    elif os == "Windows":
        return WindowsButton()
    else:
        raise ValueError


# ---- Facade ----------


class Cutter(object):
    def cutVegetables(self):
        print("All vegetables are cut")


class Boiler(object):
    def boilVegetables(self):
        print("All vegetables are boiled")


class Cook(object):
    def prepareDish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()
        self.boiler = Boiler()
        self.boiler.boilVegetables()


cook = Cook()
print(cook.cutter.cutVegetables())