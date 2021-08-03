from encapsulation.resturant.product import Product
from encapsulation.resturant.food.soup import Soup
from encapsulation.resturant.beverage.beverage import Beverage
from encapsulation.resturant.beverage.coffee import Coffee

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)

cafe = Coffee("Mokka", 0.21)
print(cafe.__class__.__bases__[0].__name__)
print(cafe.__class__.__name__)  # type(cafe).__name__
print(cafe.__class__.__base__.__name__)
print(cafe.__class__.__base__.__base__.__name__)
print(cafe.__class__.__base__.__base__.__base__.__name__)

dri = cafe.__class__.__base__.__base__("water", 0.5, 200)
print(dri.__class__.__name__)
print(dri.family_name)
