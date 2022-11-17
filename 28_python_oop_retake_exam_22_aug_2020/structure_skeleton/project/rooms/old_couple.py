from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.stove import Stove
from project.appliances.fridge import Fridge


class OldCouple(Room):
    def __init__(self, name: str, pension_one: float, pension_two: float):
        super().__init__(name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), TV(), Stove(), Stove(), Fridge(), Fridge()]
        self.calculate_expenses(self.appliances)
