from project.computer_types.computer import Computer
from math import log2


class Laptop(Computer):
    def configure_computer(self, processor: str, ram: int):
        processors = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }
        rams = [2, 4, 8, 16, 32, 64]

        if processor not in processors:
            raise ValueError(f'{processor} is not compatible with laptop {self.manufacturer} {self.model}!')
        if ram not in rams:
            raise ValueError(f'{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!')
        self.processor = processor
        self.ram = ram
        self.price += processors[processor] + self.find_power(ram) * 100
        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'
