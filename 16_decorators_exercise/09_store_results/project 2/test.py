from project.computer_store_app import ComputerStoreApp

computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.build_computer("Desktop Computer", "Apple", "Macbook", "AMD Ryzen 7 5700G", 64))
print(computer_store.sell_computer(2000, "Apple M1 Pro", 64))
print(computer_store.sell_computer(2000, "AMD Ryzen 7 5700G", 64))
print(computer_store.profit)

store = ComputerStoreApp()

build_result = store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64)
sell_result = store.sell_computer(10000, "Apple M1 Pro", 32)

print(build_result, "\nCreated Apple Macbook with Apple M1 Pro and 64GB RAM for 1800$.")
print(sell_result, "\nApple Macbook with Apple M1 Pro and 64GB RAM sold for 10000$.")
