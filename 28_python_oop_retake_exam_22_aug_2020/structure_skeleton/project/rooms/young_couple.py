from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge


class YoungCouple(Room):
    def __init__(self, name: str, salary_one: float, salary_two: float):
        super().__init__(name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), TV(), Laptop(), Laptop(), Fridge(), Fridge()]
        self.calculate_expenses(self.appliances)
