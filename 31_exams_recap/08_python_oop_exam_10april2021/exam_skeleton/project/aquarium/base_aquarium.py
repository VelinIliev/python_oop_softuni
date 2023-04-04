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
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    @abstractmethod
    def add_fish(self, fish: object):
        ...

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        output = [f"{self.name}:",
                  f"Fish: {' '.join(f.name for f in self.fish) if self.fish else 'none'}",
                  f"Decorations: {len(self.decorations)}",
                  f"Comfort: {self.calculate_comfort()}"]
        return "\n".join(output)
