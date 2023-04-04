from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    def __init__(self, name: str, price: float, portion=200):
        super().__init__(name, portion, price)

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
