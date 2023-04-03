from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository

astronauts_mapper = {
    "Biologist": Biologist,
    "Geodesist": Geodesist,
    "Meteorologist": Meteorologist
}


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in astronauts_mapper:
            raise Exception(f'Astronaut type is not valid!')

        astronaut = next(filter(lambda x: x.name == name, self.astronaut_repository.astronauts), None)

        if astronaut:
            return f'{name} is already added.'

        new_astronaut = astronauts_mapper[astronaut_type](name)

        self.astronaut_repository.add(new_astronaut)

        return f'Successfully added {astronaut_type}: {new_astronaut.name}.'

    def add_planet(self, name: str, items: str):

        planet = self.planet_repository.find_by_name(name)

        if planet:
            return f'{name} is already added.'

        new_planet = Planet(name)
        new_planet.items = items.split(", ")

        self.planet_repository.add(new_planet)

        return f'Successfully added Planet: {new_planet.name}.'

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
            raise Exception("Invalid planet name!")

        astronauts_on_mission = filter(lambda x: x.oxygen > 30, self.astronaut_repository.astronauts)
        astronauts_on_mission = sorted(astronauts_on_mission, key=lambda x: -x.oxygen)[:5:]

        if not astronauts_on_mission:
            raise Exception(f'You need at least one astronaut to explore the planet!')

        for count, astronaut in enumerate(astronauts_on_mission, 1):
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
                if not planet.items:
                    self.successful_missions += 1
                    return f'Planet: {planet.name} was explored. {count} astronauts participated in collecting items.'

        self.not_completed_missions += 1
        return f'Mission is not completed.'

    def report(self):
        output = [f'{self.successful_missions} successful missions!',
                  f'{self.not_completed_missions} missions were not completed!',
                  f"Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            output.append(f'Name: {astronaut.name}')
            output.append(f'Oxygen: {astronaut.oxygen}')
            output.append(f'Backpack items: {", ".join(astronaut.backpack) if astronaut.backpack else "none"}')

        return "\n".join(output)
