from project.train.train import Train
import unittest


class TrainTests(unittest.TestCase):
    def setUp(self) -> None:
        self.train = Train("Train", 2)

    def test_initialisation(self):
        self.assertEqual("Train", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_correct(self):
        expected = 'Added passenger Ivan'
        actual = self.train.add("Ivan")
        self.assertEqual(expected, actual)
        self.train.add("Petar")
        self.assertEqual(['Ivan', 'Petar'], self.train.passengers)

    def test_add_overload(self):
        self.train.add("Ivan")
        self.train.add("Petar")
        with self.assertRaises(ValueError) as ve:
            self.train.add("Gosho")
        expected = "Train is full"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(['Ivan', 'Petar'], self.train.passengers)

    def test_add_existing_passenger(self):
        self.train.add("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.train.add("Ivan")
        expected = 'Passenger Ivan Exists'
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(['Ivan'], self.train.passengers)

    def test_remove_correct(self):
        self.train.add("Ivan")
        self.train.add("Petar")
        expected = "Removed Ivan"
        actual = self.train.remove("Ivan")
        self.assertEqual(expected, actual)
        self.assertEqual(["Petar"], self.train.passengers)

    def test_remove_non_existing_passenger(self):
        self.train.add("Ivan")
        self.train.add("Petar")
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Gosho")
        expected = "Passenger Not Found"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(['Ivan', 'Petar'], self.train.passengers)


if __name__ == "__main__":
    unittest.main()
