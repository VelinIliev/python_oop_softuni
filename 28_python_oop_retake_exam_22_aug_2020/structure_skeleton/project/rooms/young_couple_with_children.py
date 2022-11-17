from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge


class YoungCoupleWithChildren(Room):
    def __init__(self, name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = self.create_appliances()
        self.calculate_expenses(self.appliances, self.children)

    def create_appliances(self):
        appliances = []
        for member in range(self.members_count):
            appliances.append(TV())
            appliances.append(Fridge())
            appliances.append(Laptop())
        return appliances
