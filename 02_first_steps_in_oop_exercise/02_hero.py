class Hero:
    def __init__(self, name: str, health: int):
        name = name
        health = health

    def defend(self, damage: int):
        health -= damage
        if health <= 0:
            health = 0
            return f'{name} was defeated'

    def heal(self, amount: int):
        health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
