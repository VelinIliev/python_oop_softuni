from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float, size=3):
        super().__init__(name, species, size, price)
        self.aquarium_type = "FreshwaterAquarium"

    def eat(self):
        self.size += 3
