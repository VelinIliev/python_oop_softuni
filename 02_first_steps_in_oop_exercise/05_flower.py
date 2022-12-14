class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int):
        self.is_happy = quantity >= self.water_requirements

    def status(self):
        status = ""
        if self.is_happy:
            status = "is happy"
        else:
            status = "is not happy"
        return f'{self.name} {status}'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
flower.water(120)
print(flower.status())
