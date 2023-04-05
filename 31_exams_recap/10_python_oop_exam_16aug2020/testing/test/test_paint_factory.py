from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.pf = PaintFactory("PF", 10)

    def test_initialization(self):
        self.assertEqual("PF", self.pf.name)
        self.assertEqual(10, self.pf.capacity)
        expected = ["white", "yellow", "blue", "green", "red"]
        actual = self.pf.valid_ingredients
        self.assertEqual(expected, actual)
        self.assertEqual({}, self.pf.ingredients)

    def test_add_ingredient_with_not_enough_space_raises_value_error(self):
        self.pf.capacity = 0
        with self.assertRaises(ValueError) as ve:
            self.pf.add_ingredient("white", 1)
        self.assertEqual("Not enough space in factory", str(ve.exception))
        self.assertEqual({}, self.pf.ingredients)

    def test_add_ingredient_with_non_valid_ingredient_type_error(self):
        with self.assertRaises(TypeError) as te:
            self.pf.add_ingredient("black", 1)
        expected = 'Ingredient of type black not allowed in PaintFactory'
        self.assertEqual(expected, str(te.exception))
        self.assertEqual({}, self.pf.ingredients)

    def test_add_ingredient_correct(self):
        self.pf.add_ingredient("white", 1)
        self.pf.add_ingredient("blue", 2)
        self.assertEqual({"white": 1, "blue": 2}, self.pf.ingredients)

    def test_remove_ingredient_non_existing_ingredient_raises_key_error(self):
        self.pf.add_ingredient("white", 1)
        self.pf.add_ingredient("blue", 2)
        with self.assertRaises(KeyError) as ke:
            self.pf.remove_ingredient("black", 1)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))
        self.assertEqual({"white": 1, "blue": 2}, self.pf.ingredients)

    def test_remove_ingredient_with_invalid_quantity_raises_value_error(self):
        self.pf.add_ingredient("white", 1)
        self.pf.add_ingredient("blue", 2)
        with self.assertRaises(ValueError) as ve:
            self.pf.remove_ingredient("white", 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))
        self.assertEqual({"white": 1, "blue": 2}, self.pf.ingredients)

    def test_remove_ingredient_correct(self):
        self.pf.add_ingredient("white", 1)
        self.pf.add_ingredient("blue", 2)
        self.pf.remove_ingredient("blue", 1)
        self.assertEqual({"white": 1, "blue": 1}, self.pf.ingredients)

    def test_products(self):
        self.pf.add_ingredient("white", 1)
        self.pf.add_ingredient("blue", 2)
        self.assertEqual({'white': 1, 'blue': 2}, self.pf.products)

    def test_can_add_correct(self):
        self.assertEqual(True, self.pf.can_add(2))

    def test_can_add_incorrect(self):
        self.assertEqual(False, self.pf.can_add(11))

    def test_repr(self):
        self.pf.add_ingredient("white", 1)
        self.pf.add_ingredient("blue", 2)
        expected = 'Factory name: PF with capacity 10.\n' \
                   'white: 1\n' \
                   'blue: 2\n'
        self.assertEqual(expected, self.pf.__repr__())


if __name__ == "__main__":
    main()
