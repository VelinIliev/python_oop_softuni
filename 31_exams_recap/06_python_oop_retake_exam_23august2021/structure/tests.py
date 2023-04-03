from project.space_station import SpaceStation

st = SpaceStation()
st.add_astronaut("Biologist", "Ivan")
st.add_astronaut("Biologist", "Ivan4")
st.add_astronaut("Geodesist", "Ivan2")
st.add_astronaut("Geodesist", "Ivan5")
st.add_astronaut("Meteorologist", "Ivan3")
st.add_astronaut("Meteorologist", "Ivan6")
print(st.astronaut_repository.astronauts)

print(st.add_planet("Mars", "test1, test2"))
# print(st.planet_repository.planets[0].items)
# print(st.planet_repository.planets[0].name)

# print(st.retire_astronaut("Ivan"))
print(st.astronaut_repository.astronauts)
print(st.send_on_mission("Mars"))
print(st.report())