class Shop:
    def __init__(self, name: str, items: list):
        name = name
        items = items

    def get_items_count(self):
        return len(items)

shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
