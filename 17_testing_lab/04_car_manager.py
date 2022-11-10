class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class CarTests(unittest.TestCase):
    def test_correct_initialisation(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual("a", car.make)
        self.assertEqual("b", car.model)
        self.assertEqual(1, car.fuel_consumption)
        self.assertEqual(4, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_incorrect_car_make(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "b", 1, 4)
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_incorrect_car_model(self):
        with self.assertRaises(Exception) as ex:
            car = Car("a", "", 1, 4)
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            car = Car("a", "b", -1, 4)
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            car = Car("a", "b", 1, -4)
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_negative_fuel_amount(self):
        car = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -2
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_correct_refuel(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(0, car.fuel_amount)
        car.refuel(1)
        self.assertEqual(1, car.fuel_amount)

    def test_negative_refuel(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(0, car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            car.refuel(-1)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_zero_refuel(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(0, car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_correct_drive(self):
        car = Car("a", "b", 1, 4)
        car.refuel(1)
        car.drive(1)
        self.assertEqual(0.99, car.fuel_amount)

    def test_drive_without_needed_fuel(self):
        car = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car.drive(1)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()