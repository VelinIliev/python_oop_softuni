from project.computer_types.computer import Computer


class Laptop(Computer):
    processors = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    rams = [2, 4, 8, 16, 32, 64]
    computer_type = 'laptop'



