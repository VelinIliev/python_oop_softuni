import unittest

from project.bookstore import Bookstore


class BookstoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_initialization(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_book_limit_with_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        expected = f"Books limit of 0 is not valid"
        self.assertEqual(expected, str(ve.exception))

    def test_book_limit_with_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1
        expected = f"Books limit of -1 is not valid"
        self.assertEqual(expected, str(ve.exception))

    def test_count_books(self):
        self.assertEqual(0, self.bookstore.__len__())
        self.bookstore.availability_in_store_by_book_titles = {
            "book1": 2,
            "book2": 1
        }
        self.assertEqual(3, self.bookstore.__len__())

    def test_receive_book_with_no_space_in_book_store_raises_exception(self):
        self.bookstore.receive_book("book3", 10)
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("book4", 1)
        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(ex.exception))

    def test_receive_book_correct_with_non_existing_book(self):
        actual = self.bookstore.receive_book("book3", 3)
        expected = f'3 copies of book3 are available in the bookstore.'
        self.assertEqual(expected, actual)
        self.assertEqual({"book3": 3}, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_correct_with_existing_book(self):
        self.bookstore.receive_book("book3", 3)
        actual = self.bookstore.receive_book("book3", 3)
        expected = f'6 copies of book3 are available in the bookstore.'
        self.assertEqual(expected, actual)
        self.assertEqual({"book3": 6}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_with_non_existing_book_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {"book3": 3}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book2", 1)
        expected = f"Book book2 doesn't exist!"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(0, self.bookstore.total_sold_books)
        self.assertEqual({"book3": 3}, self.bookstore.availability_in_store_by_book_titles)

    def test_test_sell_book_with_non_available_copies_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {"book3": 3}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book3", 4)
        expected = "book3 has not enough copies to sell. Left: 3"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(0, self.bookstore.total_sold_books)
        self.assertEqual({"book3": 3}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_correct(self):
        self.bookstore.availability_in_store_by_book_titles = {"book3": 3}
        expected = 'Sold 2 copies of book3'
        actual = self.bookstore.sell_book("book3", 2)
        self.assertEqual(expected, actual)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual({"book3": 1}, self.bookstore.availability_in_store_by_book_titles)

    def test__str__(self):
        self.bookstore.receive_book("book2", 1)
        self.bookstore.receive_book("book3", 2)
        self.bookstore.receive_book("book4", 2)
        self.bookstore.sell_book("book4", 2)
        expected = 'Total sold books: 2\nCurrent availability: 3\n' \
                   ' - book2: 1 copies\n' \
                   ' - book3: 2 copies\n' \
                   ' - book4: 0 copies'
        self.assertEqual(expected, str(self.bookstore))


if __name__ == "__main__":
    unittest.main()
