class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, type: str, sound: str):
        name = name
        type = type
        sound = sound

    def make_sound(self):
        return f'{name} makes {sound}'

    def get_kingdom(self):
        return __kingdom

    def info(self):
        return f'{name} is of type {type}'

mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
