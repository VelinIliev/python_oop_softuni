from abc import ABC


class Computer(ABC):
    processors = {}
    rams = {}
    computer_type = ''

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
        if not value.strip():
            raise ValueError('Manufacturer name cannot be empty.')
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError('Model name cannot be empty.')
        self.__model = value

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processors:
            raise ValueError(f'{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!')
        if ram not in self.rams:
            raise ValueError(f'{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!')

        self.processor = processor
        self.ram = ram
        self.price += self.processors[processor] + self.find_power(ram) * 100

        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'

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
