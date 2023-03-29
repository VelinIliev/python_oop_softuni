import unittest

from project.toy_store import ToyStore


class ToyStoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.ts = ToyStore()

    def test_initialization(self):
        self.assertEqual(7, len(self.ts.toy_shelf))

    def test_add_toy_with_non_existing_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy("Z", "some toy")
        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_with_already_added_toy_raise_exception(self):
        self.ts.toy_shelf["A"] = "some toy"
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy("A", "some toy")
        expected = "Toy is already in shelf!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_with_already_taken_shelf_raise_exception(self):
        self.ts.toy_shelf["A"] = "some toy"
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy("A", "other toy")
        expected = "Shelf is already taken!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_correct(self):
        actual = self.ts.add_toy("A", "some toy")
        expected = f"Toy:some toy placed successfully!"
        self.assertEqual(expected, actual)
        self.assertEqual("some toy", self.ts.toy_shelf["A"])

    def test_remove_toy_with_non_existing_shelf_raises_exception(self):
        self.ts.toy_shelf["A"] = "some toy"
        with self.assertRaises(Exception) as ex:
            self.ts.remove_toy("Z", "some toy")
        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_toy_with_wrong_name_raises_exception(self):
        self.ts.toy_shelf["A"] = "some toy"
        with self.assertRaises(Exception) as ex:
            self.ts.remove_toy("A", "other toy")
        expected = "Toy in that shelf doesn't exists!"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_toy_correct(self):
        self.ts.toy_shelf["A"] = "some toy"
        actual = self.ts.remove_toy("A", "some toy")
        expected = f"Remove toy:some toy successfully!"
        self.assertEqual(expected, actual)
        self.assertEqual(None, self.ts.toy_shelf["A"])


if __name__ == "__main__":
    unittest.main()
