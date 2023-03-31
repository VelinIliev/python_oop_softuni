from unittest import TestCase, main

from project.movie import Movie


class MovieTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Die Hard", 2002, 5.5)
        self.movie2 = Movie("Die Hard 2", 2005, 5.2)

    def test_initialization(self):
        self.movie.actors = ["Bruce Willis"]
        self.assertEqual("Die Hard", self.movie.name)
        self.assertEqual(2002, self.movie.year)
        self.assertEqual(5.5, self.movie.rating)
        self.assertEqual(["Bruce Willis"], self.movie.actors)

    def test_initialization_with_empty_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        expected = "Name cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual("Die Hard", self.movie.name)

    def test_initialization_with_non_valid_year_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        expected = "Year is not valid!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(2002, self.movie.year)

    def test_add_actor_correct(self):
        actual = self.movie.add_actor("Bruce Willis")
        expected = None
        self.assertEqual(expected, actual)
        self.assertEqual(["Bruce Willis"], self.movie.actors)

    def test_add_actor_with_existing_actor(self):
        self.movie.add_actor("Bruce Willis")
        actual = self.movie.add_actor("Bruce Willis")
        expected = "Bruce Willis is already added in the list of actors!"
        self.assertEqual(expected, actual)
        self.assertEqual(["Bruce Willis"], self.movie.actors)

    def test__gt__(self):
        actual = self.movie.__gt__(self.movie2)
        expected = '"Die Hard" is better than "Die Hard 2"'
        self.assertEqual(expected, actual)

    def test__gt__reverse(self):
        actual = self.movie2.__gt__(self.movie)
        expected = '"Die Hard" is better than "Die Hard 2"'
        self.assertEqual(expected, actual)

    def test__repr__(self):
        self.movie.add_actor("Bruce Willis")
        self.movie.add_actor("Sandra Bullock")
        expected = "Name: Die Hard\n" \
                   "Year of Release: 2002\n" \
                   "Rating: 5.50\n" \
                   "Cast: Bruce Willis, Sandra Bullock"
        actual = self.movie.__repr__()
        self.assertEqual(expected, actual)


if __name__ == "_main__":
    main()
