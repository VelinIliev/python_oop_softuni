from project.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name, portion, brand, price=2.50):
        super().__init__(name, portion, price, brand)