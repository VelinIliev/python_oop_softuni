from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("Train1", 10)

    def test_initialization(self):
        self.assertEqual("Train1", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_with_train_full_raises_value_error(self):
        self.train.capacity = 1
        self.train.add("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.train.add("Petkan")
        self.assertEqual("Train is full", str(ve.exception))
        self.assertEqual(["Ivan"], self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))

    def test_add_with_existing_passenger_raises_value_error(self):
        self.train.add("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.train.add("Ivan")
        self.assertEqual("Passenger Ivan Exists", str(ve.exception))
        self.assertEqual(["Ivan"], self.train.passengers)

    def test_add_correct(self):
        self.train.add("Ivan")
        self.assertEqual(["Ivan"], self.train.passengers)

    def test_remove_non_existing_passenger_raises_value_error(self):
        self.train.add("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Petkan")
        self.assertEqual("Passenger Not Found", str(ve.exception))
        self.assertEqual(["Ivan"], self.train.passengers)

    def test_remove_correct(self):
        self.train.add("Ivan")
        self.train.add("Petkan")
        self.assertEqual("Removed Petkan", self.train.remove("Petkan"))
        self.assertEqual(["Ivan"], self.train.passengers)


if __name__ == "__main__":
    main()
