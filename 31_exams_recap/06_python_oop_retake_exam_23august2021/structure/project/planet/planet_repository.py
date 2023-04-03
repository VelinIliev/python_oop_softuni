from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        planet = next(filter(lambda x: x.name == name, self.planets), None)
        return planet
