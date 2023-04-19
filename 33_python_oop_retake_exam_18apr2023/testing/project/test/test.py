from unittest import TestCase, main

from project.robot import Robot


class RobotTest(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("1", 'Military', 10, 100)

    def test_initialisation(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_initialisation_with_wrong_category_raises_value_error(self):
        expected = "Category should be one of '[\'Military\', \'Education\', \'Entertainment\', \'Humanoids\']'"
        with self.assertRaises(ValueError) as ve:
            robot2 = Robot("1", 'Militarys', 10, 100)
        self.assertEqual(expected, str(ve.exception))

    def test_initialisation_with_negative_price_raises_value_error(self):
        expected = "Price cannot be negative!"
        with self.assertRaises(ValueError) as ve:
            robot2 = Robot("1", 'Military', 10, -10)
        self.assertEqual(expected, str(ve.exception))

    def test_upgrade_with_existing_hardware(self):
        self.robot.upgrade("Test", 10)
        expected = 'Robot 1 was not upgraded.'
        actual = self.robot.upgrade("Test", 10)
        self.assertEqual(expected, actual)
        self.assertEqual(["Test"], self.robot.hardware_upgrades)
        self.assertEqual(115, self.robot.price)

    def test_upgrade_correct(self):
        expected = 'Robot 1 was upgraded with Test.'
        actual = self.robot.upgrade("Test", 10)
        self.assertEqual(expected, actual)
        self.assertEqual(["Test"], self.robot.hardware_upgrades)
        self.assertEqual(115, self.robot.price)

    def test_update_without_capacity(self):
        expected = "Robot 1 was not updated."
        actual = self.robot.update(10, 20)
        self.assertEqual(expected, actual)
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(10, self.robot.available_capacity)

    def test_updates_with_lower_version(self):
        self.robot.update(10, 5)
        expected = "Robot 1 was not updated."
        actual = self.robot.update(9, 2)
        self.assertEqual(expected, actual)
        self.assertEqual([10], self.robot.software_updates)
        self.assertEqual(5, self.robot.available_capacity)

    def test_updates_correct(self):
        actual = self.robot.update(10, 5)
        expected = "Robot 1 was updated to version 10."
        self.assertEqual(expected, actual)
        self.assertEqual([10], self.robot.software_updates)
        self.assertEqual(5, self.robot.available_capacity)

    def test__gt__(self):
        robot2 = Robot("2", 'Military', 10, 110)
        expected = 'Robot with ID 1 is cheaper than Robot with ID 2.'
        actual = self.robot > robot2
        self.assertEqual(expected, actual)

        robot3 = Robot("2", 'Military', 10, 90)
        expected = "Robot with ID 1 is more expensive than Robot with ID 2."
        actual = self.robot > robot3
        self.assertEqual(expected, actual)

        robot4 = Robot("2", 'Military', 10, 100)
        expected = "Robot with ID 1 costs equal to Robot with ID 2."
        actual = self.robot > robot4
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
