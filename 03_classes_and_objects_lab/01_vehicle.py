class Vehicle:
    def __init__(self, mileage, max_speed=150):
        max_speed = max_speed
        mileage = mileage
        gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
