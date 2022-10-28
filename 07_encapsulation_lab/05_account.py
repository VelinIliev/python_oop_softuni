class Account:
    def __init__(self, id: int, balance: int, pin: int):
        __id = id
        balance = balance
        __pin = pin

    def get_id(self, pin):
        if pin != __pin:
            return f'Wrong pin'
        else:
            return __id

    def change_pin(self, old_pin, new_pin):
        if old_pin == __pin:
            __pin = new_pin
            return f'Pin changed'
        else:
            return f'Wrong pin'


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
