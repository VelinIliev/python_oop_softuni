from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.fish.saltwater_fish import SaltwaterFish
from project.fish.freshwater_fish import FreshwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def find_aquarium(self, name):
        return next(filter(lambda x: x.name == name, self.aquariums), None)

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ['FreshwaterAquarium', 'SaltwaterAquarium']:
            return 'Invalid aquarium type.'
        if aquarium_type == "FreshwaterAquarium":
            new_aquarium = FreshwaterAquarium(aquarium_name)
        else:
            new_aquarium = SaltwaterAquarium(aquarium_name)
        self.aquariums.append(new_aquarium)
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            new_decoration = Ornament()
            self.decorations_repository.add(new_decoration)
            return f'Successfully added {decoration_type}.'
        elif decoration_type == "Plant":
            new_decoration = Plant()
            self.decorations_repository.add(new_decoration)
            return f'Successfully added {decoration_type}.'
        else:
            return f'Invalid decoration type.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        current_aquarium = self.find_aquarium(aquarium_name)
        current_decoration = self.decorations_repository.find_by_type(decoration_type)
        if not current_decoration:
            return f"There isn't a decoration of type {decoration_type}."
        if current_aquarium:
            current_aquarium.add_decoration(current_decoration)
            self.decorations_repository.remove(current_decoration)
            return f'Successfully added {decoration_type} to {current_aquarium.name}.'

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ['FreshwaterFish', 'SaltwaterFish']:
            return f"There isn't a fish of type {fish_type}."
        current_aquarium = self.find_aquarium(aquarium_name)
        if not current_aquarium:
            return
        if len(current_aquarium.fish) == current_aquarium.capacity:
            return f'Not enough capacity.'
        if current_aquarium.suitable_for != fish_type:
            return f'Water not suitable.'
        if fish_type == "FreshwaterFish":
            new_fish = FreshwaterFish(fish_name, fish_species, price)
            current_aquarium.add_fish(new_fish)
        else:
            new_fish = SaltwaterFish(fish_name, fish_species, price)
            current_aquarium.add_fish(new_fish)
        return f'Successfully added {fish_type} to {aquarium_name}.'

    def feed_fish(self, aquarium_name: str):
        current_aquarium = self.find_aquarium(aquarium_name)
        if not current_aquarium:
            return
        current_aquarium.feed()
        return f'Fish fed: {len(current_aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):
        current_aquarium = self.find_aquarium(aquarium_name)
        if not current_aquarium:
            return
        fishes_sum = 0
        decorations_sum = 0
        if current_aquarium.fish:
            for fish in current_aquarium.fish:
                fishes_sum += fish.price
        if current_aquarium.decorations:
            for decoration in current_aquarium.decorations:
                decorations_sum += decoration.price
        return f"The value of Aquarium {aquarium_name} is {fishes_sum + decorations_sum:.2f}."

    def report(self):
        return "\n".join(str(a) for a in self.aquariums)
