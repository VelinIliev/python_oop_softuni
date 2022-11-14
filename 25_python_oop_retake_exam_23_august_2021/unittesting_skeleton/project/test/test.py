import unittest

from project.library import Library
import unittest


class LibraryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library("Hristo Botev")

    def test_initialisation(self):
        self.assertEqual("Hristo Botev", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_wrong_name(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_no_existing_author(self):
        self.library.add_book("Ivan Vazov", "Pod igoto")
        expected = {'Ivan Vazov': ['Pod igoto']}
        self.assertEqual(expected, self.library.books_by_authors)

    def test_add_book_existing_author(self):
        self.library.add_book("Ivan Vazov", "Pod igoto")
        self.library.add_book("Ivan Vazov", "Chichovci")
        expected = {'Ivan Vazov': ['Pod igoto', "Chichovci"]}
        self.assertEqual(expected, self.library.books_by_authors)

    def test_add_reader_non_registered(self):
        self.library.add_reader("Velin")
        self.assertEqual({"Velin": []}, self.library.readers)

    def test_add_reader_registered(self):
        self.library.add_reader("Velin")
        expected = 'Velin is already registered in the Hristo Botev library.'
        actual = self.library.add_reader("Velin")
        self.assertEqual(expected, actual)

    def test_rent_book_correct(self):
        self.library.add_book("Ivan Vazov", "Pod igoto")
        self.library.add_reader("Velin")
        self.library.rent_book("Velin", "Ivan Vazov", "Pod igoto")
        expected = {'Velin': [{'Ivan Vazov': 'Pod igoto'}]}
        self.assertEqual(expected, self.library.readers)
        self.assertEqual({'Ivan Vazov': []}, self.library.books_by_authors)

    def test_rent_book_non_existing_user(self):
        self.library.add_book("Ivan Vazov", "Pod igoto")
        self.library.add_reader("Velin")
        actual = self.library.rent_book("Ivan", "Ivan Vazov", "Pod igoto")
        expected = f'Ivan is not registered in the Hristo Botev Library.'
        self.assertEqual(expected, actual)
        self.assertEqual({'Velin': []}, self.library.readers)
        self.assertEqual({'Ivan Vazov': ['Pod igoto']}, self.library.books_by_authors)

    def test_rent_book_non_existing_author(self):
        self.library.add_book("Ivan Vazov", "Pod igoto")
        self.library.add_reader("Velin")
        actual = self.library.rent_book("Velin", "Hristo Botev", "Molitva")
        expected = f"Hristo Botev Library does not have any Hristo Botev's books."
        self.assertEqual(expected, actual)
        self.assertEqual({'Velin': []}, self.library.readers)
        self.assertEqual({'Ivan Vazov': ['Pod igoto']}, self.library.books_by_authors)

    def test_rent_book_non_existing_book(self):
        self.library.add_book("Ivan Vazov", "Pod igoto")
        self.library.add_reader("Velin")
        actual = self.library.rent_book("Velin", "Ivan Vazov", "Chichovci")
        expected = f"""Hristo Botev Library does not have Ivan Vazov's "Chichovci"."""
        self.assertEqual(expected, actual)
        self.assertEqual({'Velin': []}, self.library.readers)
        self.assertEqual({'Ivan Vazov': ['Pod igoto']}, self.library.books_by_authors)
