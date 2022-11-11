from project.shopping_cart import ShoppingCart
import unittest


class ShoppingCartTests(unittest.TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Name", 200)

    def test_initialisation_correct(self):
        self.assertEqual("Name", self.shopping_cart.shop_name)
        self.assertEqual(200, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_shop_name_no_capital_letter(self):
        with self.assertRaises(ValueError) as ve:
            new_sc = ShoppingCart("name", 200)
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    def test_shop_name_numbers(self):
        with self.assertRaises(ValueError) as ve:
            new_sc = ShoppingCart("Name23", 200)
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_correct(self):
        expected = "cheese product was successfully added to the cart!"
        actual = self.shopping_cart.add_to_cart("cheese", 2)
        self.assertEqual(expected, actual)
        self.assertEqual({'cheese': 2}, self.shopping_cart.products)

    def test_add_to_cart_with_price_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("cheese", 100)
        expected = 'Product cheese cost too much!'
        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_with_price_error2(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("cheese", 105)
        expected = 'Product cheese cost too much!'
        self.assertEqual(expected, str(ve.exception))

    def test_remove_from_cart_non_existing_product(self):
        self.shopping_cart.add_to_cart("meat", 3)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("cheese")
        expected = 'No product with name cheese in the cart!'
        self.assertEqual(expected, str(ve.exception))

    def test_remove_from_cart_correct(self):
        self.shopping_cart.add_to_cart("cheese", 2)
        self.shopping_cart.add_to_cart("meat", 3)
        expected = 'Product cheese was successfully removed from the cart!'
        actual = self.shopping_cart.remove_from_cart("cheese")
        self.assertEqual(expected, actual)
        self.assertEqual({"meat": 3}, self.shopping_cart.products)

    def test__add__(self):
        shopping_cart_2 = ShoppingCart("NameTwo", 300)
        self.shopping_cart.add_to_cart("cheese", 2)
        shopping_cart_2.add_to_cart("food", 3)
        new_shopping_cart = self.shopping_cart.__add__(shopping_cart_2)
        self.assertEqual("NameNameTwo", new_shopping_cart.shop_name)
        self.assertEqual(500, new_shopping_cart.budget)
        self.assertEqual({'cheese': 2, 'food': 3}, new_shopping_cart.products)

    def test_buy_products_correct(self):
        self.shopping_cart.add_to_cart("cheese", 2)
        expected = 'Products were successfully bought! Total cost: 2.00lv.'
        actual = self.shopping_cart.buy_products()
        self.assertEqual(expected, actual)

    def test_buy_product_incorrect(self):
        self.shopping_cart.add_to_cart("cheese", 99)
        self.shopping_cart.add_to_cart("meat", 99)
        self.shopping_cart.add_to_cart("food", 3)

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        expected = 'Not enough money to buy the products! Over budget with 1.00lv!'
        self.assertEqual(expected, str(ve.exception))

    def test_buy_product_eq_to_budget(self):
        self.shopping_cart.add_to_cart("cheese", 99)
        self.shopping_cart.add_to_cart("meat", 99)
        self.shopping_cart.add_to_cart("food", 2)
        expected = 'Products were successfully bought! Total cost: 200.00lv.'
        actual = self.shopping_cart.buy_products()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

# TODO: Not ready 92/100