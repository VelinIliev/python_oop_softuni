from project.motorcycle import Motorcycle

class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    # def drive(self, kilometers: int):
    #     needed_fuel = kilometers * self.fuel_consumption
    #     if self.fuel - needed_fuel >= 0:
    #         self.fuel -= needed_fuel
