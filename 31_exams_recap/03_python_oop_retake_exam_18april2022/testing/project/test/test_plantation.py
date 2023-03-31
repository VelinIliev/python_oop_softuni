from unittest import TestCase, main

from project.plantation import Plantation


class PlantationTest(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(3)

    def test_initialization(self):
        self.assertEqual(3, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_with_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_already_hired_raises_value_error(self):
        self.plantation.workers.append("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Ivan")
        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["Ivan"], self.plantation.workers)

    def test_hire_worker_correct(self):
        expected = f'Ivan successfully hired.'
        actual = self.plantation.hire_worker("Ivan")
        self.assertEqual(expected, actual)
        self.assertEqual(["Ivan"], self.plantation.workers)

    def test__len__(self):
        self.plantation.plants = {"Ivan": ["plant1", "plant3"], "Petkan": ["plant3"]}
        self.assertEqual(3, self.plantation.__len__())

    def test_planting_with_non_existing_worker_raises_value_error(self):
        self.plantation.workers = ["Petkan"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "plant1")
        expected = 'Worker with name Ivan is not hired!'
        self.assertEqual(expected, str(ve.exception))

    def test_planting_with_full_plantation_raises_value_error(self):
        self.plantation.workers = ["Petkan"]
        self.plantation.planting("Petkan", "plant1")
        self.plantation.planting("Petkan", "plant2")
        self.plantation.planting("Petkan", "plant3")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Petkan", "plant4")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_correct_for_first_time(self):
        self.plantation.workers = ["Petkan"]
        actual = self.plantation.planting("Petkan", "plant1")
        expected = "Petkan planted it's first plant1."
        self.assertEqual(expected, actual)

    def test_planting_correct(self):
        self.plantation.workers = ["Petkan"]
        self.plantation.planting("Petkan", "plant1")
        actual = self.plantation.planting("Petkan", "plant2")
        expected = 'Petkan planted plant2.'
        self.assertEqual(expected, actual)

    def test__str__(self):
        self.plantation.workers = ["Petkan"]
        self.plantation.planting("Petkan", "plant1")
        expected = "Plantation size: 3\nPetkan\nPetkan planted: plant1"
        actual = self.plantation.__str__()
        self.assertEqual(expected, actual)

    def test__repr__(self):
        self.plantation.workers = ["Petkan"]
        self.plantation.planting("Petkan", "plant1")
        expected = "Size: 3\nWorkers: Petkan"
        actual = self.plantation.__repr__()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
