class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


import unittest
from unittest import TestCase


class CatTests(TestCase):
    def test_cat_size_after_eating(self):
        cat = Cat("Tom")
        cat.eat()
        self.assertEqual(cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        cat = Cat("Tom")
        cat.eat()
        self.assertEqual(cat.fed, True)

    def test_if_cat_cannot_eat_if_fed(self):
        cat = Cat("Tom")
        cat.eat()
        with self.assertRaises(Exception) as exception:
            cat.eat()
        self.assertEqual('Already fed.', str(exception.exception))

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        cat = Cat("Tom")
        with self.assertRaises(Exception) as exception:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(exception.exception))

    def test_cat_isnot_sleepy_after_sleeping(self):
        cat = Cat("Tom")
        cat.eat()
        cat.sleep()
        self.assertEqual(cat.sleepy, False)


if __name__ == "__main__":
    unittest.main()