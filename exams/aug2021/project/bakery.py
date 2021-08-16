from exams.aug2021.project.baked_food.bread import Bread
from exams.aug2021.project.baked_food.cake import Cake
from exams.aug2021.project.drink.tea import Tea
from exams.aug2021.project.drink.water import Water
from exams.aug2021.project.table.inside_table import InsideTable
from exams.aug2021.project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        else:
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand:str):
        if name in [d.name for d in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
        else:
            self.drinks_menu.append(Water(name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        else:
            self.tables_repository.append(OutsideTable(table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = [t for t in self.tables_repository if (not t.is_reserved) and (t.capacity >= number_of_people)]
        if table:
            table[0].reserve(number_of_people)
            return f"Table {table[0].table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        food_yes = []
        food_no = set()
        for name in food_names:
            if name in [f.name for f in self.food_menu]:
                food = [f for f in self.food_menu if f.name == name][0]
                food_yes.append(food)
                table[0].order_food(food)
            else:
                food_no.add(name)
        result = f"Table {table_number} ordered:\n"
        for f in food_yes:
            result += f"{f}\n"
        if not food_no:
            return result
        result += f"{self.name} does not have in the menu:\n"
        for fn in food_no:
            result += f"{fn}\n"
        return result

    def order_drink(self, table_number: int, *drink_names):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        drink_yes = []
        drink_no = set()
        for name in drink_names:
            if name in [d.name for d in self.drinks_menu]:
                drink = [d for d in self.drinks_menu if d.name == name][0]
                drink_yes.append(drink)
                table[0].order_drink(drink)
            else:
                drink_no.add(name)
        result = f"Table {table_number} ordered:\n"
        for d in drink_yes:
            result += f"{d}\n"
        if not drink_no:
            return result
        result += f"{self.name} does not have in the menu:\n"
        for fn in drink_no:
            result += f"{fn}\n"
        return result

    def leave_table(self, table_number):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            bill = table.get_bill()
            self.total_income += bill
            table.clear()
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if table.free_table_info():
                result += f"{table.free_table_info()}\n"
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
