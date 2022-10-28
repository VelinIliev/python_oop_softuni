from project.beverage.beverage import Beverage
from project.food.soup import Soup
from project.product import Product

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

# zero test
from project.product import Product
from project.beverage.beverage import Beverage
from project.food.soup import Soup
import unittest

class Tests(unittest.TestCase):
   def test(self):
       product = Product("coffee", 2.5)
       print(product.__class__.__name__, "Product")
       print(product.name, "coffee")
       print(product.price, 2.5)
       beverage = Beverage("coffee", 2.5, 50)
       print(beverage.__class__.__name__, "Beverage")
       print(beverage.__class__.__bases__[0].__name__, "Product")
       print(beverage.name, "coffee")
       print(beverage.price, 2.5)
       print(beverage.milliliters, 50)
       soup = Soup("fish soup", 9.90, 230)
       print(soup.__class__.__name__, "Soup")
       print(soup.__class__.__bases__[0].__name__, "Starter")
       print(soup.name, "fish soup")
       print(soup.price, 9.90)
       print(soup.grams, 230)

if __name__ == "__main__":
   unittest.main()