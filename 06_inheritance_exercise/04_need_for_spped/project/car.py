from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    # def drive(self, kilometers: int):
    #     needed_fuel = kilometers * self.fuel_consumption
    #     if self.fuel - needed_fuel >= 0:
    #         self.fuel -= needed_fuel