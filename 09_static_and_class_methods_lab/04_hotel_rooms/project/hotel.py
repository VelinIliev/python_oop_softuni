from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def from_stars(stars_count: int):
        return Hotel(str(f'{stars_count} stars Hotel'))

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if not isinstance(room.take_room(people), str):
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                guests = room.free_room()
                if not isinstance(guests, str):
                    self.guests -= guests

    def status(self):
        return_string = ""
        return_string += f'Hotel {self.name} has {self.guests} total guests\n'
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        return_string += f'Free rooms: {", ".join(str(x) for x in free_rooms)}\n'
        return_string += f'Taken rooms: {", ".join(str(x) for x in taken_rooms)}'
        return return_string



