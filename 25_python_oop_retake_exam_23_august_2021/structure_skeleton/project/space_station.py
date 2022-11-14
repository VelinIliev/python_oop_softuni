from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.meteorologist import Meteorologist
from project.astronaut.geodesist import Geodesist
from project.planet.planet import Planet


class SpaceStation:
    number_of_successful_missions = 0
    number_of_not_completed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type == "Biologist" or astronaut_type == "Geodesist" or astronaut_type == "Meteorologist":
            for astronaut in self.astronaut_repository.astronauts:
                if astronaut.name == name:
                    return f'{name} is already added.'
            if astronaut_type == "Biologist":
                new_astronaut = Biologist(name)
                self.astronaut_repository.add(new_astronaut)
                return f'Successfully added {astronaut_type}: {name}.'
            elif astronaut_type == "Geodesist":
                new_astronaut = Geodesist(name)
                self.astronaut_repository.add(new_astronaut)
                return f'Successfully added {astronaut_type}: {name}.'
            elif astronaut_type == "Meteorologist":
                new_astronaut = Meteorologist(name)
                self.astronaut_repository.add(new_astronaut)
                return f'Successfully added {astronaut_type}: {name}.'
        else:
            raise Exception('Astronaut type is not valid!')

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f'{name} is already added.'
        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.add(new_planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception(f'Invalid planet name!')
        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True)
        astronauts_on_mission = []
        for i, astronaut in enumerate(sorted_astronauts, 1):
            if i <= 5 and astronaut.oxygen > 30:
                astronauts_on_mission.append(astronaut)
        if not astronauts_on_mission:
            raise Exception(f'You need at least one astronaut to explore the planet!')
        for i, astronaut in enumerate(astronauts_on_mission, 1):
            while astronaut.oxygen > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
                if not planet.items:
                    self.number_of_successful_missions += 1
                    return f'Planet: {planet_name} was explored. {i} ' \
                           f'astronauts participated in collecting items.'
        self.number_of_not_completed_missions += 1
        return f'Mission is not completed.'

    def report(self):
        display_list = []
        display_list.append(f"{self.number_of_successful_missions} successful missions!")
        display_list.append(f"{self.number_of_not_completed_missions} missions were not completed!")
        display_list.append(f"Astronauts' info:")
        for astronaut in self.astronaut_repository.astronauts:
            display_list.append(f'Name: {astronaut.name}')
            display_list.append(f'Oxygen: {astronaut.oxygen}')
            if astronaut.backpack:
                display_list.append(f'Backpack items: {", ".join(astronaut.backpack)}')
            else:
                display_list.append(f'Backpack items: none')
        return "\n".join(display_list)
