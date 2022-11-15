from project.pet_shop import PetShop
import unittest


class PetShopTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Зоомагазин")

    def test_initialisation(self):
        self.assertEqual("Зоомагазин", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_correct(self):
        self.pet_shop.add_food("riba",  1)
        self.pet_shop.add_food("Meso",  1)
        expected = f'Successfully added 1.00 grams of Meso.'
        actual = self.pet_shop.add_food("Meso",  1)
        self.assertEqual(expected, actual)
        self.assertEqual({'riba': 1, 'Meso': 2}, self.pet_shop.food)

    def test_add_food_zero_quantity(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("riba", 0)
        expected = f'Quantity cannot be equal to or less than 0'
        self.assertEqual(expected, str(ve.exception))

    def test_add_pet_correct(self):
        expected = 'Successfully added Gosho.'
        actual = self.pet_shop.add_pet("Gosho")
        self.assertEqual(expected, actual)

    def test_add_pet_with_existing_pet(self):
        self.pet_shop.add_pet("Gosho")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Gosho")
        expected = "Cannot add a pet with the same name"
        self.assertEqual(expected, str(ex.exception))

    def test_feed_correct(self):
        self.pet_shop.add_pet("Gosho")
        self.pet_shop.add_food("Meso", 1000)
        expected = 'Gosho was successfully fed'
        actual = self.pet_shop.feed_pet("Meso", "Gosho")
        self.assertEqual(expected, actual)
        self.assertEqual({'Meso': 900}, self.pet_shop.food)

    def test_feed_with_non_existing_pet(self):
        self.pet_shop.add_pet("Gosho")
        self.pet_shop.add_food("Meso", 1000)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Meso", "Tosho")
        expected = 'Please insert a valid pet name'
        self.assertEqual(expected, str(ex.exception))

    def test_feed_wit_non_existing_food(self):
        self.pet_shop.add_pet("Gosho")
        self.pet_shop.add_food("Meso", 1000)
        actual = self.pet_shop.feed_pet("riba", "Gosho")
        expected = 'You do not have riba'
        self.assertEqual(expected, actual)

    def test_feed_with_small_amount_of_food(self):
        self.pet_shop.add_pet("Gosho")
        self.pet_shop.add_food("Meso", 90)
        actual = self.pet_shop.feed_pet("Meso", "Gosho")
        expected = 'Adding food...'
        self.assertEqual(expected, actual)
        self.assertEqual({'Meso': 1090.0}, self.pet_shop.food)

    def test_repr(self):
        self.pet_shop.add_pet("Gosho")
        self.pet_shop.add_food("Meso", 9)
        expected = 'Shop Зоомагазин:\nPets: Gosho'
        actual = self.pet_shop.__repr__()
        self.assertEqual(expected, actual)
