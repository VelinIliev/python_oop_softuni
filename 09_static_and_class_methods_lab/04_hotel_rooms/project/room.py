class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if self.is_taken is not True and people <= self.capacity:
            self.is_taken = True
            self.guests = people
            return people
        return f'Room number {self.number} cannot be taken'

    def free_room(self):
        if self.is_taken:
            guests = self.guests
            self.is_taken = False
            self.guests = 0
            return guests
        return f'Room number {self.number} is not taken'
