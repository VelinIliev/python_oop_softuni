from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    # def drive(self, kilometers: int):
    #     needed_fuel = kilometers * self.fuel_consumption
    #     if self.fuel - needed_fuel >= 0:
    #         self.fuel -= needed_fuel