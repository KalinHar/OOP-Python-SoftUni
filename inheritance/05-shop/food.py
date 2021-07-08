from project.product import Product
# form settings import FOOD_QUANTITY

class Food(Product):
    def __init__(self, name, quantity=15):
        super().__init__(name, quantity)

    # def __init__(self, name):  # version - 2  THE BEST
    #     super().__init__(name, FOOD_QUANTITY)

    # def __init__(self, name):  # version - 3
    #     super().__init__(name, 15)
