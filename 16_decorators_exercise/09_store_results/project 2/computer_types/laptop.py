from project.computer_types.computer import Computer


class Laptop(Computer):
    processors = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    rams = [2, 4, 8, 16, 32, 64]

    def configure_computer(self, processor, ram):
        if processor not in self.processors:
            raise ValueError(f'{processor} is not compatible with laptop {self.manufacturer} {self.model}!')
        if ram not in self.rams:
            raise ValueError(f'{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!')
        self.processor = processor
        self.price += self.processors[processor]
        self.ram = ram
        self.price += self.find_power(ram) * 100
        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'




