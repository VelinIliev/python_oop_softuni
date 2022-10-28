class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        name = name
        type = type
        capacity = capacity
        items = {}

    @staticmethod
    def small_shop(name: str, type: str):
        new_shop = Shop(name, type, 10)
        return new_shop

    def add_item(self, item_name: str):
        if item_name in items and items[item_name] < capacity:
            items[item_name] += 1
            return f'{item_name} added to the shop'
        elif item_name not in items:
            items[item_name] = 1
            return f'{item_name} added to the shop'
        else:
            return f'Not enough capacity in the shop'

    def remove_item(self, item_name: str, amount: int):
        if item_name in items and items[item_name] - amount >= 0:
            items[item_name] -= amount
            if items[item_name] == 0:
                del items[item_name]
            return f'{amount} {item_name} removed from the shop'
        else:
            return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{name} of type {type} with capacity {capacity}'


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)
#
print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))
#
print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
