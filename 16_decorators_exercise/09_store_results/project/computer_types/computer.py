from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        test_value = value.replace(" ", "")
        if test_value == "":
            raise ValueError('Manufacturer name cannot be empty.')
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        test_value = value.replace(" ", "")
        if test_value == "":
            raise ValueError('Model name cannot be empty.')
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor, ram):
        ...

    def __repr__(self):
        return f'{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM'

    @staticmethod
    def find_power(number):
        number = number
        powers = 0
        while number >= 2:
            number = number / 2
            powers += 1
        return powers
