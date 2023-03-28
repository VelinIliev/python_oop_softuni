import unittest

from project.truck_driver import TruckDriver


class TruckDriverTests(unittest.TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver("Ivan", 10)

    def test_initialisation_correct(self):
        self.assertEqual("Ivan", self.truck_driver.name)
        self.assertEqual(10, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_add_cargo_offer_correct(self):
        expected = f"Cargo for 2 to London was added as an offer."
        actual = self.truck_driver.add_cargo_offer("London", 2)
        self.assertEqual(expected, actual)
        self.assertEqual({'London': 2}, self.truck_driver.available_cargos)

    def test_add_cargo_offer_existing_location(self):
        self.truck_driver.add_cargo_offer("London", 2)
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("London", 2)
        expected = "Cargo offer is already added."
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({'London': 2}, self.truck_driver.available_cargos)

    def test_drive_best_cargo_offer_correct(self):
        self.truck_driver.add_cargo_offer("London", 2)
        self.truck_driver.add_cargo_offer("Paris", 10)
        expected = f"Ivan is driving 10 to Paris."
        actual = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(expected, actual)
        self.assertEqual(100, self.truck_driver.earned_money)
        self.assertEqual(10, self.truck_driver.miles)

    def test_drive_best_cargo_offer_with_no_locations(self):
        self.truck_driver.drive_best_cargo_offer()
        expected = f"There are no offers available."
        actual = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_check_for_activities_with_no_money(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.check_for_activities(250)
        expected = f"Ivan went bankrupt."
        self.assertEqual(expected, str(ve.exception))

    def test_check_for_activities_with_eat(self):
        self.truck_driver.add_cargo_offer("London", 250)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(2480, self.truck_driver.earned_money)

    def test_check_for_activities_with_sleep(self):
        self.truck_driver.add_cargo_offer("London", 1000)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(9875, self.truck_driver.earned_money)
        # print(self.truck_driver.earned_money)

    def test_check_for_activities_with_gas(self):
        self.truck_driver.add_cargo_offer("London", 1500)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(14335, self.truck_driver.earned_money)
        # print(self.truck_driver.earned_money)

    def test_check_for_activities_with_repair(self):
        self.truck_driver.add_cargo_offer("London", 10000)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(88250, self.truck_driver.earned_money)
        # print(self.truck_driver.earned_money)

    def test_repr(self):
        expected = 'Ivan has 0 miles behind his back.'
        actual = self.truck_driver.__repr__()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
