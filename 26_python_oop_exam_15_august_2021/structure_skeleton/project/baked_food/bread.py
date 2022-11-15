from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    def __init__(self, name, price, portion=200):
        super().__init__(name, portion, price)