from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    processors = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }
    rams = [2, 4, 8, 16, 32, 64, 128]

    def configure_computer(self, processor, ram):
        if processor not in self.processors:
            raise ValueError(f'{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!')
        if ram not in self.rams:
            raise ValueError(f'{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!')
        self.processor = processor
        self.price += self.processors[processor]
        self.ram = ram
        self.price += self.find_power(ram) * 100
        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'

