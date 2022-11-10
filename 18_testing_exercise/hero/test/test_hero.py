from project.hero import Hero
import unittest


class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Username", 1, 100, 2)
        self.enemy = Hero("Username2", 2, 100, 3)

    def test_initialisation(self):
        self.assertEqual("Username", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(2, self.hero.damage)

    def test_battle_with_same_username(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_no_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_enemy_with_no_health(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual('You cannot fight Username2. He needs to rest', str(ve.exception))

    def test_battle_hero_loose(self):
        self.assertEqual("You lose", str(self.hero.battle(self.enemy)))
        self.assertEqual(94, self.hero.health )
        self.assertEqual(103, self.enemy.health )

    def test_battle_hero_win(self):
        self.hero.damage = 100
        self.assertEqual("You win", str(self.hero.battle(self.enemy)))
        self.assertEqual(99, self.hero.health)
        self.assertEqual(0, self.enemy.health)

    def test_battle_draw(self):
        self.hero.damage = 100
        self.enemy.damage = 100
        self.assertEqual("Draw", str(self.hero.battle(self.enemy)))

    def test_str(self):
        expected = f"Hero Username: 1 lvl\n"\
                   f"Health: 100\n" \
                   f"Damage: 2\n"
        result = str(self.hero)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()