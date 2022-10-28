class Product:
    def __init__(self, name: str, price: float):
        __name = name
        __price = price

    @property
    def name(self):
        return __name

    @property
    def price(self):
        return __price
