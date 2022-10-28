from topping import Topping
from dough import Dough


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        # if name == "":
        #     raise ValueError("The name cannot be an empty string")
        # if dough is None:
        #     raise ValueError("You should add dough to the pizza")
        # if toppings_capacity <= 0:
        #     raise ValueError("The topping's capacity cannot be less or equal to zero")
        name = name
        dough = dough
        toppings_capacity = toppings_capacity
        toppings = {}

    @property
    def name(self):
        return __name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        __name = value

    @property
    def dough(self):
        return __dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        __dough = value

    @property
    def toppings_capacity(self):
        return __toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        __toppings_capacity = value

    def add_topping(self, topping: Topping):
        if len(toppings) == toppings_capacity:
            raise ValueError(f'Not enough space for another topping')
        if topping.topping_type in toppings:
            toppings[topping.topping_type] += topping.weight
        else:
            toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = dough.weight + sum(toppings.values())
        return total_weight
