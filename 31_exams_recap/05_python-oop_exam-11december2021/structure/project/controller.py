from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race

car_mapper = {
    "MuscleCar": MuscleCar,
    "SportsCar": SportsCar
}


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):

        car = next(filter(lambda x: x.model == model, self.cars), None)

        if car:
            raise Exception(f'Car {model} is already created!')

        if car_type in car_mapper:
            new_car = car_mapper[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):

        driver = next(filter(lambda x: x.name == driver_name, self.drivers), None)

        if driver:
            raise Exception(f'Driver {driver_name} is already created!')

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f'Driver {new_driver.name} is created.'

    def create_race(self, race_name: str):

        race = next(filter(lambda x: x.name == race_name, self.races), None)

        if race:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f'Race {new_race.name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):

        driver = next(filter(lambda x: x.name == driver_name, self.drivers), None)

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        car = next(filter(lambda x: x.__class__.__name__ == car_type and x.is_taken == False, self.cars[::-1]), None)

        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            driver.car.is_taken = True

            return f'Driver {driver_name} changed his car from {old_car.model} to {driver.car.model}.'

        driver.car = car
        car.is_taken = True

        return f'Driver {driver_name} chose the car {driver.car.model}.'

    def add_driver_to_race(self, race_name: str, driver_name: str):

        driver = next(filter(lambda x: x.name == driver_name, self.drivers), None)

        race = next(filter(lambda x: x.name == race_name, self.races), None)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        if not driver.car:
            raise Exception(f'Driver {driver.name} could not participate in the race!')

        if driver in race.drivers:
            return f'Driver {driver.name} is already added in {race.name} race.'

        race.drivers.append(driver)

        return f'Driver {driver.name} added in {race.name} race.'

    def start_race(self, race_name: str):
        race = next(filter(lambda x: x.name == race_name, self.races), None)

        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if len(race.drivers) < 3:
            raise Exception(f'Race {race.name} cannot start with less than 3 participants!')

        winners = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3:]

        output = []

        for driver in winners:
            driver.number_of_wins += 1
            output.append(f'Driver {driver.name} wins the {race.name} race with a speed of {driver.car.speed_limit}.')

        return "\n".join(output)
