from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float, size=5):
        super().__init__(name, species, size, price)
        self.live_in = "SaltwaterAquarium"

    def eat(self):
        self.size += 2