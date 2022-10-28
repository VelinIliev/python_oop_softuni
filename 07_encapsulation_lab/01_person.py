class Person:
    def __init__(self, name: str, age: int):
        __name = name
        __age = age

    def get_name(self):
        return __name

    def get_age(self):
        return __age


person = Person("Ivan", 14)
print(person.get_name())
print(person.get_age())