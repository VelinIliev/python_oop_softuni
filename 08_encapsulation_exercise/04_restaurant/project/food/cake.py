from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str):
        super().__init__(name, PRICE, GRAMS, CALORIES)
        __calories = CALORIES

    @property
    def calories(self):
        return __calories
