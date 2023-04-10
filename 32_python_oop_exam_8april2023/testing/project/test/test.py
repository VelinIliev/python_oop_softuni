from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TennisPlayerTests(TestCase):
    def setUp(self) -> None:
        self.tp = TennisPlayer("Ivan", 24, 100)

    def test_initialization(self):
        self.assertEqual("Ivan", self.tp.name)
        self.assertEqual(24, self.tp.age)
        self.assertEqual(100, self.tp.points)
        self.assertEqual([], self.tp.wins)

    def test_player_with_wrong_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tp.name = "Iv"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_player_with_wrong_age_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tp.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_correct(self):
        self.tp.add_new_win("Sofia Open")
        self.assertEqual(['Sofia Open'], self.tp.wins)

    def test_add_win_with_existing_win(self):
        self.tp.add_new_win("Sofia Open")
        expected = f'Sofia Open has been already added to the list of wins!'
        actual = self.tp.add_new_win("Sofia Open")
        self.assertEqual(expected, actual)
        self.assertEqual(['Sofia Open'], self.tp.wins)

    def test__lt__(self):
        tp2 = TennisPlayer("Petkan", 28, 50)
        expected = 'Ivan is a top seeded player and he/she is better than Petkan'
        actual = self.tp > tp2
        self.assertEqual(expected, actual)

    def test__lt__2(self):
        tp2 = TennisPlayer("Petkan", 28, 50)
        expected = "Ivan is a better player than Petkan"
        actual = tp2 > self.tp
        self.assertEqual(expected, actual)

    def test__str__(self):
        self.tp.add_new_win("Sofia Open")
        self.tp.add_new_win("Plovdiv Open")
        # print(self.tp)
        expected = f'Tennis Player: Ivan\n' \
                   f'Age: 24\n' \
                   f'Points: 100.0\n' \
                   f'Tournaments won: Sofia Open, Plovdiv Open'
        actual = self.tp.__str__()
        self.assertEqual(expected, actual)


if __name__ == "__mian__":
    main()
