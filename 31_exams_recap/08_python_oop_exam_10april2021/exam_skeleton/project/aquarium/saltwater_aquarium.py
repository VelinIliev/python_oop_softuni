from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name: str, capacity=25):
        super().__init__(name, capacity)

    def add_fish(self, fish: object):
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'

        fish_type = fish.__class__.__name__
        if fish_type == "SaltwaterFish":
            self.fish.append(fish)
            return f"Successfully added {fish_type} to {self.name}."
