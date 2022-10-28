class Animal:
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        name = name
        gender = gender
        age = age
        money_for_care = money_for_care

    def __repr__(self):
        return f'Name: {name}, Age: {age}, Gender: {gender}'