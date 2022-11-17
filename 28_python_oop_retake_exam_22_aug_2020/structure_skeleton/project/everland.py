class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: object):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses
            total_consumption += room.room_cost
        return f'Monthly consumption: {total_consumption:.2f}$.'

    def pay(self):
        rooms_to_remove = []
        display_list = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= room.expenses + room.room_cost
                display_list.append(f'{room.family_name} paid {room.expenses+room.room_cost:.2f}$ and have {room.budget:.2f}$ left.')
            else:
                rooms_to_remove.append(room)
                display_list.append(f'{room.family_name} does not have enough budget and must leave the hotel.')
        for room in rooms_to_remove:
            self.rooms.remove(room)
        return "\n".join(display_list)

    def status(self):
        display_list = []
        total_people = sum(x.members_count for x in self.rooms)
        display_list.append(f'Total population: {total_people}')
        for room in self.rooms:
            display_list.append(str(room))
        return '\n'.join(display_list)
    # Total population: {all_people_in_the_hotel}
    # {room_name} with {members} members. Budget: {current_budget}$, Expenses: {expenses}$
    # --- Child {n} monthly cost: {cost_for_one_month}$
    # … {rest of the children if any}
    # --- Appliances monthly cost: {cost_of_all_appliances_for_one_month}$
    # … {rest of the rooms if any}