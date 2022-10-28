class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        fuel_consumption = DEFAULT_FUEL_CONSUMPTION
        fuel = fuel
        horse_power = horse_power

    def drive(self, kilometers: int):
        needed_fuel = kilometers * fuel_consumption
        if fuel - needed_fuel >= 0:
            fuel -= needed_fuel
