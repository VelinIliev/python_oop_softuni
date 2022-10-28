from .. import Product


class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        __milliliters = milliliters

    @property
    def milliliters(self):
        return __milliliters

