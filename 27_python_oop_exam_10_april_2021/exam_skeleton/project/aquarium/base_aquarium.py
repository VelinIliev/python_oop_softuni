from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError('Aquarium name cannot be an empty string.')
        self.__name = value

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish: object):
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'
        fish_type = fish.__class__.__name__
        if fish_type in ("FreshwaterFish", "SaltwaterFish"):
            self.fish.append(fish)
            return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        display_list = []
        display_list.append(f'{self.name}:')
        if self.fish:
            display_list.append(f'Fish: {" ".join(x.name for x in self.fish)}')
        else:
            display_list.append(f'Fish: none')
        display_list.append(f'Decorations: {len(self.decorations)}')
        display_list.append(f'Comfort: {self.calculate_comfort()}')
        return "\n".join(display_list)

