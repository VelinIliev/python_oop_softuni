from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.family_name = family_name
        self.budget = salary_one + salary_two
        self.room_cost = 30
        self.children = [*children]
        self.members_count = 2 + len(self.children)
        self.appliances = []
        for _ in range(self.members_count):
            self.appliances.append(TV())
            self.appliances.append(Fridge())
            self.appliances.append(Laptop())
        self.calculate_expenses(*self.appliances, *self.children)
