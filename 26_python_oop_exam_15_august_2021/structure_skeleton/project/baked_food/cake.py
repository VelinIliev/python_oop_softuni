from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    def __init__(self, name, price, portion=245):
        super().__init__(name, portion, price)