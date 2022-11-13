from project.movie import Movie
import unittest

class MovieTests(unittest.TestCase):

    def test_correct_initialisation(self):
        movie = Movie("XXX", 2008, 5.1)
        self.assertEqual("XXX", movie.name)
        self.assertEqual(2008, movie.year)
        self.assertEqual(5.1, movie.rating)
        self.assertEqual([], movie.actors)

    def test_initialisation_with_no_name(self):
        with self.assertRaises(ValueError) as ve:
            movie = Movie("", 2008, 5.1)
        expected = 'Name cannot be an empty string!'
        self.assertEqual(expected, str(ve.exception))

    def test_initialisation_with_wrong_year(self):
        with self.assertRaises(ValueError) as ve:
            movie = Movie("XXX", 1886, 5.1)
        expected = 'Year is not valid!'
        self.assertEqual(expected, str(ve.exception))

    def test_add_actor_correct(self):
        movie = Movie("XXX", 2008, 5.1)
        movie.add_actor("Velin")
        self.assertEqual(["Velin"], movie.actors)

    def test_add_actor_with_existing_actor(self):
        movie = Movie("XXX", 2008, 5.1)
        movie.add_actor("Velin")

        expected = 'Velin is already added in the list of actors!'
        self.assertEqual(expected, movie.add_actor("Velin"))

    def test_gt_(self):
        movie = Movie("XXX", 2008, 5.1)
        movie2 = Movie("XXA", 2008, 3.1)
        expected = '"XXX" is better than "XXA"'
        self.assertEqual(expected, movie.__gt__(movie2))
        self.assertEqual(expected, movie2.__gt__(movie))

    def test__repr(self):
        movie = Movie("XXX", 2008, 5.1)
        movie.add_actor("Velin")
        movie.add_actor("Ivan")
        expected = 'Name: XXX\n' \
                   'Year of Release: 2008\n' \
                   'Rating: 5.10\n' \
                   'Cast: Velin, Ivan'
        self.assertEqual(expected, movie.__repr__())

if __name__ == "__main__":
    unittest.main()