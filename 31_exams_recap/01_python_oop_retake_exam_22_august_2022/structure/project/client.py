class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0
        self.temp_order = []

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.startswith("0") or not value.isnumeric() or not len(value) == 10:
            raise ValueError('Invalid phone number!')
        self.__phone_number = value
