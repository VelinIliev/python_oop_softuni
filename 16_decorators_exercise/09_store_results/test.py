from project.computer_store_app import ComputerStoreApp

# computer_store = ComputerStoreApp()
# print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
# print(computer_store.build_computer("Desktop Computer", "Apple", "Macbook", "AMD Ryzen 7 5700G", 64))
# print(computer_store.sell_computer(2000, "Apple M1 Pro", 64))
# print(computer_store.sell_computer(2000, "AMD Ryzen 7 5700G", 64))
# print(computer_store.profits)
#
# store = ComputerStoreApp()
#
# build_result = store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64)
# sell_result = store.sell_computer(1800, "Apple M1 Pro", 64)
#
# print(build_result, "\nCreated Apple Macbook with Apple M1 Pro and 64GB RAM for 1800$.")
# print(sell_result, "\nApple Macbook with Apple M1 Pro and 64GB RAM sold for 10000$.")
# print(store.profits)
# from project.computer_store_app import ComputerStoreApp
#
# computer_store = ComputerStoreApp()
# print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
# print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))


import math
#
#
# def ram_is_valid(ram):
#     if 0 < ram <= 128:
#         while ram != 1:
#             if ram % 2 != 0:
#                 return False
#             ram = ram // 2
#         return True
#     return False
#
#
# def ram_price(ram):
#     return int(math.log2(ram) * 100)
#
#
# print(ram_is_valid(22))
# print(ram_price(16))

from unittest import TestCase, main
from project.computer_store_app import ComputerStoreApp


# class TestComputerStoreAppClass(TestCase):
#     def test_practice(self):
#         self.store = ComputerStoreApp()
#
#         build_result = self.store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64)
#         sell_result = self.store.sell_computer(10000, "Apple M1 Pro", 32)
#
#         self.assertEqual(build_result, "Created Apple Macbook with Apple M1 Pro and 64GB RAM for 1800$.")
#         self.assertEqual(sell_result, "Apple Macbook with Apple M1 Pro and 64GB RAM sold for 10000$.")

store = ComputerStoreApp()

build_result = store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64)
sell_result = store.sell_computer(10000, "Apple M1 Pro", 32)

print(build_result, "Created Apple Macbook with Apple M1 Pro and 64GB RAM for 1800$.")
print(sell_result, "Apple Macbook with Apple M1 Pro and 64GB RAM sold for 10000$.")



