import unittest

from project.shopping_cart import ShoppingCart


class ShoppingCartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.shop = ShoppingCart("NewShop", 100)

    def test_initialization(self):
        self.assertEqual("NewShop", self.shop.shop_name)
        self.assertEqual(100, self.shop.budget)
        self.shop.products = {'Product1': 50}
        self.assertEqual({'Product1': 50}, self.shop.products)

    def test_new_shop_name_with_small_first_letter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = "newShop"
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual("NewShop", self.shop.shop_name)

    def test_new_shop_name_with_with_number_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = "newShop1"
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual("NewShop", self.shop.shop_name)

    def test_add_to_cart_correct(self):
        expected = 'Product product was successfully added to the cart!'
        actual = self.shop.add_to_cart("Product", 50)
        self.assertEqual(expected, actual)
        self.assertEqual({'Product': 50}, self.shop.products)

    def test_add_to_cart_with_expensive_product_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart("Product", 100)
        expected = 'Product Product cost too much!'
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({}, self.shop.products)

    def test_remove_from_cart_correct(self):
        self.shop.add_to_cart("Product1", 50)
        self.shop.add_to_cart("Product2", 50)
        expected = 'Product Product1 was successfully removed from the cart!'
        actual = self.shop.remove_from_cart("Product1")
        self.assertEqual(expected, actual)
        self.assertEqual({"Product2": 50}, self.shop.products)

    def test_remove_from_cart_with_non_existing_product_raises_value_error(self):
        self.shop.add_to_cart("Product2", 50)
        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart("Product1")
        expected = 'No product with name Product1 in the cart!'
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({"Product2": 50}, self.shop.products)

    def test__add__correct(self):
        self.shop2 = ShoppingCart("OldShop", 100)
        self.shop.add_to_cart("Product1", 50)
        self.shop2.add_to_cart("Product2", 50)
        self.shop3 = self.shop.__add__(self.shop2)
        self.assertEqual('NewShopOldShop', self.shop3.shop_name)
        self.assertEqual(200, self.shop3.budget)
        self.assertEqual({"Product1":  50, "Product2": 50}, self.shop3.products)

    def test_buy_products_correct(self):
        self.shop.add_to_cart("Product1", 10)
        self.shop.add_to_cart("Product2", 20)
        expected = 'Products were successfully bought! Total cost: 30.00lv.'
        actual = self.shop.buy_products()
        self.assertEqual(expected, actual)

    def test_buy_products_with_smallest_budget_raises_value_error(self):
        self.shop.add_to_cart("Product1", 90)
        self.shop.add_to_cart("Product2", 20)
        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()
        expected = 'Not enough money to buy the products! Over budget with 10.00lv!'
        self.assertEqual(expected, str(ve.exception))
