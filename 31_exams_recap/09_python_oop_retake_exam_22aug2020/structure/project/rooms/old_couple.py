from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float, members_count=2):
        self.family_name = family_name
        self.budget = pension_one + pension_two
        self.members_count = members_count
        self.room_cost = 15
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
        self.calculate_expenses(*self.appliances)
        self.children = []
