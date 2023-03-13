from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, km):
        return None

    @abstractmethod
    def refuel(self, fuel):
        return None


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, km):
        fuel_used = km * (self.fuel_consumption + .9)
        if fuel_used <= self.fuel_quantity:
            self.fuel_quantity -= fuel_used

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, km):
        fuel_used = km * (self.fuel_consumption + 1.6)
        if fuel_used <= self.fuel_quantity:
            self.fuel_quantity -= fuel_used

    def refuel(self, fuel):
        fuel = fuel * .95
        self.fuel_quantity += fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

