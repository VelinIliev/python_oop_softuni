class Customer:
    id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Customer.id += 1
        return Customer.id

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'


# c = Customer("x", "X", "x")
# d = Customer("x", "X", "x")
# e = Customer("x", "X", "x")
# print(c.id)
# print(d.id)
# print(e.id)
