from project.plantation import Plantation
import unittest

class PlantationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_initialisation(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_initialisation_with_negative_size(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation2 = Plantation(-1)
        expect = 'Size must be positive number!'
        self.assertEqual(expect, str(ve.exception))

    def test_hire_worker_correct(self):
        self.plantation.hire_worker("Ivan")
        expected = 'Petar successfully hired.'
        self.assertEqual(expected, self.plantation.hire_worker("Petar"))
        self.assertEqual( ["Ivan", "Petar"], self.plantation.workers)

    def test_hire_worker_with_already_hired(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Petar")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Petar")
        expect = 'Worker already hired!'
        self.assertEqual(expect, str(ve.exception))
        self.assertEqual(["Ivan", "Petar"], self.plantation.workers)

    def test_len_(self):
        self.assertEqual(0, self.plantation.__len__())
        self.plantation.plants = {"Ivan": ["tree", "flower"], "Peter": ["flower"]}
        self.assertEqual(3, self.plantation.__len__())

    def test_planting_with_not_hired_worker(self):
        self.plantation.hire_worker("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Petar", "tree")
        expected = f'Worker with name Petar is not hired!'
        self.assertEqual(expected, str(ve.exception))

    def test_planting_with_no_capacity(self):
        self.plantation.size = 2
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Ivan", "tree")
        self.plantation.planting("Ivan", "tree")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "tree")
        expected = f'The plantation is full!'
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({'Ivan': ['tree', 'tree']}, self.plantation.plants)

    def test_planting_for_first_time(self):
        self.plantation.hire_worker("Ivan")
        expected = f"Ivan planted it's first tree."
        self.assertEqual(expected, self.plantation.planting("Ivan", "tree"))
        self.assertEqual({'Ivan': ['tree']}, self.plantation.plants)

    def test_planting_with_existing_worker(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Ivan", "tree")
        expected = 'Ivan planted tree.'
        self.assertEqual(expected, self.plantation.planting("Ivan", "tree"))
        self.assertEqual({'Ivan': ['tree', 'tree']}, self.plantation.plants)

    def test_str(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Ivan", "tree")
        expected = f'Plantation size: 10\nIvan\nIvan planted: tree'
        self.assertEqual(expected, self.plantation.__str__())

    def test_repr(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Ivan", "tree")
        expected = f'Size: 10\nWorkers: Ivan'
        self.assertEqual(expected, self.plantation.__repr__())


if __name__ == "__main__":
    unittest.main()