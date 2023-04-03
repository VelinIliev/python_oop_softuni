from unittest import TestCase, main

from project.library import Library


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library("SomeLibrary")

    def test_initialization_correct(self):
        self.assertEqual("SomeLibrary", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_initialization_with_wrong_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_with_existing_author(self):
        self.library.books_by_authors = {"Some Author": ["Some book 1", "Some book 2"]}
        self.library.readers = {"Ivan": []}
        self.library.add_book("Some Author", "Some book 3")
        actual = self.library.books_by_authors
        expected = {'Some Author': ['Some book 1', 'Some book 2', 'Some book 3']}
        self.assertEqual(expected, actual)

    def test_add_book_with_non_existing_author(self):
        self.library.books_by_authors = {"Some Author": ["Some book 1", "Some book 2"]}
        self.library.readers = {"Ivan": []}
        self.library.add_book("Some Author 2", "Some book 3")
        actual = self.library.books_by_authors
        expected = {'Some Author': ['Some book 1', 'Some book 2'], "Some Author 2": ["Some book 3"]}
        self.assertEqual(expected, actual)

    def test_add_book_with_existing_author_and_existing_book(self):
        self.library.books_by_authors = {"Some Author": ["Some book 1", "Some book 2"]}
        self.library.readers = {"Ivan": []}
        self.library.add_book("Some Author", "Some book 2")
        self.assertEqual({"Some Author": ["Some book 1", "Some book 2"]}, self.library.books_by_authors)

    def test_add_reader_non_existing(self):
        self.library.books_by_authors = {"Some Author": ["Some book 1", "Some book 2"]}
        self.library.readers = {"Ivan": []}
        self.library.add_reader("Petkan")
        self.assertEqual({"Ivan": [], "Petkan": []}, self.library.readers)

    def test_add_reader_existing(self):
        self.library.books_by_authors = {"Some Author": ["Some book 1", "Some book 2"]}
        self.library.readers = {"Ivan": []}
        actual = self.library.add_reader("Ivan")
        expected = "Ivan is already registered in the SomeLibrary library."
        self.assertEqual(expected, actual)

    def test_rent_book_with_non_existing_reader(self):
        self.library.books_by_authors = {"Some Author": ["Some book 1", "Some book 2"]}
        self.library.readers = {"Ivan": []}
        expected = "Petkan is not registered in the SomeLibrary Library."
        actual = self.library.rent_book("Petkan", "Some Author", "Some book 1")
        self.assertEqual(expected, actual)

    def test_rent_book_with_non_existing_author(self):
        self.library.books_by_authors = {"Some Author": ["Some book 1", "Some book 2"]}
        self.library.readers = {"Ivan": []}
        expected = f"SomeLibrary Library does not have any Some Author 2's books."
        actual = self.library.rent_book("Ivan", "Some Author 2", "Some book 1")
        self.assertEqual(expected, actual)

    def test_rent_book_with_non_existing_book(self):
        self.library.books_by_authors = {"Some Author": ["Some book 1", "Some book 2"]}
        self.library.readers = {"Ivan": []}
        expected = """SomeLibrary Library does not have Some Author's "Some book 3"."""
        actual = self.library.rent_book("Ivan", "Some Author", "Some book 3")
        self.assertEqual(expected, actual)

    def test_rent_book_correct(self):
        self.library.books_by_authors = {"Some Author": ["Some book 1", "Some book 2"]}
        self.library.readers = {"Ivan": []}
        self.library.rent_book("Ivan", "Some Author", "Some book 2")
        self.assertEqual({'Ivan': [{'Some Author': 'Some book 2'}]}, self.library.readers)
        self.assertEqual({'Some Author': ['Some book 1']}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
