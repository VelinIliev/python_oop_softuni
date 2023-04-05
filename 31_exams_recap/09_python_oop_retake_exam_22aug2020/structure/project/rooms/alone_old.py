from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name: str, pension: float, members_count=1):
        super().__init__(family_name, pension, members_count)
        self.room_cost = 10
        self.appliances = []
        self.children = []
