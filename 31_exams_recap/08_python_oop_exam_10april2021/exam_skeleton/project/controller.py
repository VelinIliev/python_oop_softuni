from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

aquarium_mapper = {
    "FreshwaterAquarium": FreshwaterAquarium,
    "SaltwaterAquarium": SaltwaterAquarium
}
decoration_mapper = {
    "Ornament": Ornament,
    "Plant": Plant
}
fish_mapper = {
    "FreshwaterFish": FreshwaterFish,
    "SaltwaterFish": SaltwaterFish
}


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in aquarium_mapper:
            return "Invalid aquarium type."

        new_aquarium = aquarium_mapper[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)

        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):

        if decoration_type not in decoration_mapper:
            return f'Invalid decoration type.'

        new_decoration = decoration_mapper[decoration_type]()
        self.decorations_repository.add(new_decoration)

        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = next(filter(lambda x: x.name == aquarium_name, self.aquariums), None)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium:
            aquarium.decorations.append(decoration)
            self.decorations_repository.remove(decoration)

            return f'Successfully added {decoration_type} to {aquarium_name}.'

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):

        if fish_type not in fish_mapper:
            return f"There isn't a fish of type {fish_type}."

        aquarium = next(filter(lambda x: x.name == aquarium_name, self.aquariums), None)
        new_fish = fish_mapper[fish_type](fish_name, fish_species, price)

        result = aquarium.add_fish(new_fish)

        if result is None:
            return f'Water not suitable.'

        return result

    def feed_fish(self, aquarium_name: str):

        aquarium = next(filter(lambda x: x.name == aquarium_name, self.aquariums), None)

        aquarium.feed()

        return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):

        aquarium = next(filter(lambda x: x.name == aquarium_name, self.aquariums), None)

        value_of_aquarium = sum([*[f.price for f in aquarium.fish], *[d.price for d in aquarium.decorations]])

        return f'The value of Aquarium {aquarium_name} is {value_of_aquarium:.2f}.'

    def report(self):
        return "\n".join(str(aquarium) for aquarium in self.aquariums)
