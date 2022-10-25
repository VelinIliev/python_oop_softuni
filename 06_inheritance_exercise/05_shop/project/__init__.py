# from product import Product
# from food import Food
# from drink import Drink
# from product_repository import ProductRepository
#
# food = Food("apple")
# drink = Drink("water")
# repo = ProductRepository()
# repo.add(food)
# repo.add(drink)
# print(repo.products)
# print(repo.find("water"))
# repo.find("apple").decrease(5)
# print(repo)

import unittest

# from drink import Drink
# from food import Food
# from product import Product
# from product_repository import ProductRepository
#
#
# product = Product('product', 150)
# drink = Drink('drink')
# food = Food('food')
# repo = ProductRepository()
#
# print(product.name) #, 'product'
# print(product.quantity) #, 150)
# #
# product.decrease(10)
# print(product.quantity) #, 140)
# #
# product.increase(10)
# print(product.quantity) #, 160)
# #
# print(drink.name) #, 'drink')
# print(drink.quantity) #10)
# print(drink.__class__.__base__.__name__) #, 'Product')
#
# drink.decrease(10)
# print(drink.quantity) #, 0)
# #
# drink.increase(10)
# print(drink.quantity) #, 20)
#
# print(food.name) #, 'food')
# print(food.quantity) #, 15)
# print(food.__class__.__base__.__name__) #, 'Product')
#
# food.decrease(10)
# print(food.quantity, 5)
#
# food.increase(10)
# print(food.quantity, 25)
# #
# print(repo.products, [])
# #
# repo.add(food)
# repo.add(drink)
# print(len(repo.products), 2)
# print(repo.products[0], food)
# print(repo.products[1], drink)

# repo.products = [drink, food]
# repo.remove('drink')
# print(repo.products[0], food)
# repo.remove('drink')
# print(repo.products[0], food)
# #
# repo.add(food)
# repo.add(drink)
# actual = str(repo)
# expected = 'food: 15\ndrink: 10'
# print(expected, actual)

