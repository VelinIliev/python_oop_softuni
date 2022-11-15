from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name, portion, brand, price=1.50):
        super().__init__(name, portion, price, brand)