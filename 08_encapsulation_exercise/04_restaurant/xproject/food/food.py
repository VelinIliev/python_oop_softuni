from .. import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        __grams = grams

    @property
    def grams(self):
        return __grams
