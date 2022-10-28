class Flower:
    def __init__(self, name: str, water_requirements: int):
        name = name
        water_requirements = water_requirements
        is_happy = False

    def water(self, quantity: int):
        is_happy = quantity >= water_requirements

    def status(self):
        status = ""
        if is_happy:
            status = "is happy"
        else:
            status = "is not happy"
        return f'{name} {status}'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
flower.water(120)
print(flower.status())
