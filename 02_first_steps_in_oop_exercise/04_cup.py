class Cup:
    def __init__(self, size: int, quantity: int):
        size = size
        quantity = quantity

    def fill(self, milliliters: int):
        if quantity + milliliters <= size:
            quantity += milliliters

    def status(self):
        free_space = size - quantity
        return free_space

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
