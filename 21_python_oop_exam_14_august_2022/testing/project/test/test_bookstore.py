from project.bookstore import Bookstore
import unittest

class BookstoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_initialisation(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_book_limit_less_then_0(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1
        expected = f'Books limit of -1 is not valid'
        self.assertEqual(expected, str(ve.exception))

    def test_book_limit_equal_to_0(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        expected = f'Books limit of 0 is not valid'
        self.assertEqual(expected, str(ve.exception))

    def test__len__(self):
        self.assertEqual(0, self.bookstore.__len__())
        self.bookstore.availability_in_store_by_book_titles = {"book": 2}
        self.assertEqual(2, self.bookstore.__len__())

    def test_receive_book_when_no_space(self):
        self.bookstore.availability_in_store_by_book_titles = {"book": 9}
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("book2", 2)
        expected = 'Books limit is reached. Cannot receive more books!'
        self.assertEqual(expected, str(ex.exception))

    def test_receive_new_book_correct(self):
        expected = f'2 copies of book2 are available in the bookstore.'
        self.assertEqual(expected, self.bookstore.receive_book("book2", 2))
        self.assertEqual({'book2': 2}, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_existing_book_correct(self):
        self.bookstore.receive_book("book2", 2)
        expected = f'3 copies of book2 are available in the bookstore.'
        self.assertEqual(expected, self.bookstore.receive_book("book2", 1))
        self.assertEqual({'book2': 3}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_non_existing_book(self):
        self.bookstore.receive_book("book2", 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book3", 1)
        expected = "Book book3 doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_with_not_enough_quantity(self):
        self.bookstore.receive_book("book2", 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book2", 3)
        expected = "book2 has not enough copies to sell. Left: 2"
        self.assertEqual(expected, str(ex.exception))

    def test_see_book_correct(self):
        self.bookstore.receive_book("book2", 2)
        expected = "Sold 2 copies of book2"
        self.assertEqual(expected, self.bookstore.sell_book("book2", 2))

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


