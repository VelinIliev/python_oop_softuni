from abc import ABC


class Drink(ABC):
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError(f'Name cannot be empty string or white space!')
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        if value <= 0:
            raise ValueError(f'Portion cannot be less than or equal to zero!')
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value.strip() == "":
            raise ValueError(f'Brand cannot be empty string or white space!')
        self.__brand = value

    def __repr__(self):
        return f' - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv'
