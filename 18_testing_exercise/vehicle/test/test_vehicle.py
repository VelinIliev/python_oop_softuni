from project.vehicle import Vehicle
import unittest


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(2, 10)

    def test_initialisation(self):
        self.assertEqual(2, self.vehicle.fuel)
        self.assertEqual(2, self.vehicle.capacity)
        self.assertEqual(10, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_correct(self):
        self.vehicle.drive(1)
        self.assertEqual(0.75, self.vehicle.fuel)

    def test_drive_with_no_fuel_needed(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(2)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_correct(self):
        self.vehicle.drive(1)
        self.vehicle.refuel(1)
        self.assertEqual(1.75, self.vehicle.fuel)

    def test_refuel_incorrect(self):
        self.vehicle.drive(1)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(2)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected = f'The vehicle has 10 horse power with 2 fuel left and 1.25 fuel consumption'
        result = str(self.vehicle)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()