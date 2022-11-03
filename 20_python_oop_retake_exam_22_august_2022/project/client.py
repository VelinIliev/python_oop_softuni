class Client:
    def __init__(self, phone_number: str):

        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.00
        self.temp_shopping_cart = []

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value[0] != "0" or len(value) != 10 or not value.isnumeric():
            raise ValueError('Invalid phone number!')
        self.__phone_number = value
