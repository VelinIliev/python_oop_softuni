from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses + room.room_cost
        return f'Monthly consumption: {total:.2f}$.'

    def pay(self):
        output = []
        for room in self.rooms:
            balance = room.budget - room.room_cost - room.expenses
            if balance >= 0:
                output.append(f"{room.family_name} paid {room.expenses + room.room_cost}$ and have {balance}$ left.")
                room.budget = balance
            else:
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(output)

    def status(self):
        total_population = 0

        output = [f'Total population: {total_population}', ]
        for room in self.rooms:
            total_population += room.members_count
            output.append(f'{room.family_name} with {room.members_count} members. '
                          f'Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$')
            for n, child in enumerate(room.children, 1):
                output.append(f'--- Child {n} monthly cost: {child.get_monthly_expense():.2f}$')
            appliances_cost = sum([x.get_monthly_expense() for x in room.appliances])
            output.append(f'--- Appliances monthly cost: {appliances_cost:.2f}$')
        output[0] = f'Total population: {total_population}'

        return "\n".join(output)