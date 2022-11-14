from project.space_station import SpaceStation

space_station = SpaceStation()
space_station.add_planet("Mars", "item1, item2, item3")
# print(space_station.planet_repository.planets[0].name)
# print(space_station.planet_repository.planets[0].items)

space_station.add_astronaut("Biologist", "Ivan")
space_station.add_astronaut("Geodesist", "Petkan")
space_station.add_astronaut("Meteorologist", "Joro")
space_station.send_on_mission("Mars")
print(space_station.report())
