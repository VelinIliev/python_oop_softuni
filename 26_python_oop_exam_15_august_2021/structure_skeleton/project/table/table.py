from abc import ABC, abstractmethod


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError(f'Capacity has to be greater than 0!')
        self.__capacity = value

    def reserve(self, number_of_people: int):
        if not self.is_reserved:
            self.is_reserved = True
            self.number_of_people = number_of_people

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total = 0
        for food in self.food_orders:
            total += food.price
        for drink in self.drink_orders:
            total += drink.price
        return total

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            display_list = [f'Table: {self.table_number}',
                            f'Type: {self.__class__.__name__}',
                            f'Capacity: {self.capacity}']
            return "\n".join(display_list)