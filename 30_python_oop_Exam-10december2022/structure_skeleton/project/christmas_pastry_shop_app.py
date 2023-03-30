from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen

delicacies_mapper = {
    "Gingerbread": lambda name, price: Gingerbread(name, price),
    "Stolen": lambda name, price: Stolen(name, price)
}
booths_mapper = {
    "Open Booth": lambda booth_number, capacity: OpenBooth(booth_number, capacity),
    "Private Booth": lambda booth_number, capacity: PrivateBooth(booth_number, capacity)
}


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        delicacy = next(filter(lambda x: x.name == name, self.delicacies), None)

        if delicacy:
            raise Exception(f'{name} already exists!')

        if type_delicacy not in delicacies_mapper:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        new_delicacy = delicacies_mapper[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

        return f'Added delicacy {new_delicacy.name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        booth = next(filter(lambda x: x.booth_number == booth_number, self.booths), None)

        if booth:
            raise Exception(f'Booth number {booth_number} already exists!')

        if type_booth not in booths_mapper:
            raise Exception(f'{type_booth} is not a valid booth!')

        new_booth = booths_mapper[type_booth](booth_number, capacity)
        self.booths.append(new_booth)

        return f'Added booth number {new_booth.booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):
        booth = next(filter(lambda x: x.is_reserved == False and x.capacity >= number_of_people, self.booths), None)

        if not booth:
            raise Exception(f'No available booth for {number_of_people} people!')

        booth.reserve(number_of_people)

        return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next(filter(lambda x: x.booth_number == booth_number, self.booths), None)
        delicacy = next(filter(lambda x: x.name == delicacy_name, self.delicacies), None)

        if not booth:
            raise Exception(f'Could not find booth {booth_number}!')

        if not delicacy:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        booth.delicacy_orders.append(delicacy)

        return f'Booth {booth.booth_number} ordered {delicacy.name}.'

    def leave_booth(self, booth_number: int):
        booth = next(filter(lambda x: x.booth_number == booth_number, self.booths), None)

        bill = booth.price_for_reservation
        for order in booth.delicacy_orders:
            bill += order.price

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        self.income += bill

        return f'Booth {booth.booth_number}:\n' \
               f'Bill: {bill:.2f}lv.'

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'
