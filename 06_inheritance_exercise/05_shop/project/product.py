class Product:
    def __init__(self, name: str, quantity: int):
        name = name
        quantity = quantity

    def decrease(self, quantity: int):
        if quantity - quantity >= 0:
            quantity -= quantity

    def increase(self, quantity: int):
        quantity += quantity

    def __repr__(self):
        return name