# from product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product_name == product.name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product_name == product.name:
                self.products.remove(product)
        # product = self.find(product_name)
        # if product:
        #     self.products.remove(product)

    def __repr__(self):
        return '\n'.join([pr.name + ": " + str(pr.quantity) for pr in self.products])


# ban = Product("banana", 5)
# can = Product("cocoa", 4)
# man = Product("mango", 3)
# pp = ProductRepository()
# pp.add(ban)
# pp.add(can)
# pp.add(man)
# print(pp)
# print(pp.find("banana"))
# pp.remove("banana")
# print(pp)

