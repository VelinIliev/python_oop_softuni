from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [x for x in self.customers if x.id == customer_id][0]
        current_dvd = [x for x in self.dvds if x.id == dvd_id][0]
        is_rented = [x for x in current_customer.rented_dvds if current_dvd.id == x.id]
        if is_rented:
            return f'{current_customer.name} has already rented {current_dvd.name}'
        if current_dvd.is_rented:
            return f'DVD is already rented'
        if current_customer.age < current_dvd.age_restriction:
            return f'{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie'
        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f'{current_customer.name} has successfully rented {current_dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        current_customer = [x for x in self.customers if x.id == customer_id][0]
        if current_customer:
            for i, dvd in enumerate(current_customer.rented_dvds):
                if dvd.id == dvd_id:
                    dvd.is_rented = False
                    current_customer.rented_dvds.pop(i)
                    return f"{current_customer.name} has successfully returned {dvd.name}"
        return f'{current_customer.name} does not have that DVD'

    def __repr__(self):
        return_string = ""
        for customer in self.customers:
            return_string += f'{customer}\n'
        for dvd in self.dvds:
            return_string += f'{dvd}\n'
        return return_string

