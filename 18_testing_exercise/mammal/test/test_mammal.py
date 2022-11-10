from project.mammal import Mammal
import unittest


class MammalTests(unittest.TestCase):
    def test_initialisation(self):
        mammal = Mammal("Test", "Type", "Sound")
        self.assertEqual("Test", mammal.name)
        self.assertEqual("Type", mammal.type)
        self.assertEqual("Sound", mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound(self):
        mammal = Mammal("Test", "Type", "Sound")
        self.assertEqual(f'Test makes Sound', mammal.make_sound())

    def test_get_kingdom(self):
        mammal = Mammal("Test", "Type", "Sound")
        self.assertEqual("animals", mammal.get_kingdom())

    def test_info(self):
        mammal = Mammal("Test", "Type", "Sound")
        self.assertEqual(f"Test is of type Type", mammal.info())
