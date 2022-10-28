class Car:
    def __init__(self, name: str, model: str, engine: str):
        name = name
        model = model
        engine = engine

    def get_info(self):
        return f'This is {name} {model} with engine {engine}'


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

# car = Car("W124", "Mercedes", "Petrol l4")
# print(car.get_info())
