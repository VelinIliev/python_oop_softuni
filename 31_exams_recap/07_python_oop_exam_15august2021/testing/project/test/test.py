from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("PetShop")

    def test_initialization(self):
        self.assertEqual("PetShop", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_with_negative_quantity_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("Food", -1)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_food_with_new_food(self):
        expected = "Successfully added 100.00 grams of Food1."
        actual = self.pet_shop.add_food("Food1", 100)
        self.assertEqual(expected, actual)
        self.assertEqual({"Food1": 100}, self.pet_shop.food)

    def test_add_food_with_existing_food(self):
        self.pet_shop.add_food("Food1", 100)
        expected = "Successfully added 100.00 grams of Food1."
        actual = self.pet_shop.add_food("Food1", 100)
        self.assertEqual(expected, actual)
        self.assertEqual({"Food1": 200}, self.pet_shop.food)

    def test_add_pet_with_new_pet(self):
        actual = self.pet_shop.add_pet("Pet Name")
        expected = 'Successfully added Pet Name.'
        self.assertEqual(expected, actual)
        self.assertEqual(["Pet Name"], self.pet_shop.pets)

    def test_add_pet_with_existing_pet_raises_exception(self):
        self.pet_shop.add_pet("Pet Name")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Pet Name")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(["Pet Name"], self.pet_shop.pets)

    def test_feed_pet_with_non_existing_pet_raises_exception(self):
        self.pet_shop.add_pet("Pet Name")
        self.pet_shop.add_food("Food1", 100)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Food1", "Pet Name 2")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_non_existing_food_raises_exception(self):
        self.pet_shop.add_pet("Pet Name")
        self.pet_shop.add_food("Food1", 100)
        actual = self.pet_shop.feed_pet("Food2", "Pet Name")
        self.assertEqual("You do not have Food2", actual)

    def test_feed_pet_with_food_smallest_then_100(self):
        self.pet_shop.add_pet("Pet Name")
        self.pet_shop.add_food("Food1", 80)
        actual = self.pet_shop.feed_pet("Food1", "Pet Name")
        self.assertEqual("Adding food...", actual)
        self.assertEqual({'Food1': 1080.0}, self.pet_shop.food)

    def test_feed_pet_correct(self):
        self.pet_shop.add_pet("Pet Name")
        self.pet_shop.add_food("Food1", 200)
        actual = self.pet_shop.feed_pet("Food1", "Pet Name")
        self.assertEqual("Pet Name was successfully fed", actual)
        self.assertEqual({'Food1': 100}, self.pet_shop.food)

    def test__repr__(self):
        self.pet_shop.add_pet("Pet Name")
        self.pet_shop.add_pet("Pet Name 2")
        expected = f'Shop PetShop:\n' \
                   f'Pets: Pet Name, Pet Name 2'
        self.assertEqual(expected, self.pet_shop.__repr__())



if __name__ == "__main__":
    main()
