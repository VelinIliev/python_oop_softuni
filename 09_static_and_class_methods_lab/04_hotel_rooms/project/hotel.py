from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next(filter(lambda x: x.number == room_number, self.rooms), None)
        if room:
            if not isinstance(room.take_room(people), str):
                self.guests += people

    def free_room(self, room_number):
        room = next(filter(lambda x: x.number == room_number, self.rooms), None)
        if room:
            guests = room.free_room()
            if not isinstance(guests, str):
                self.guests -= guests

    def status(self):
        output = [f'Hotel {self.name} has {self.guests} total guests',
                  f'Free rooms: {", ".join(str(room.number) for room in self.rooms if not room.is_taken)}',
                  f'Taken rooms: {", ".join(str(room.number) for room in self.rooms if room.is_taken)}']
        return "\n".join(output)



