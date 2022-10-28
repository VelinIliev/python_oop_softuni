class Account:
    def __init__(self, id: int, name: str, balance=0):
        id = id
        name = name
        balance = balance

    def credit(self, amount):
        balance += amount
        return balance

    def debit(self, amount):
        if balance - amount >= 0:
            balance -= amount
            return balance
        else:
            return f'Amount exceeded balance'

    def info(self):
        return f'User {name} with account {id} has {balance} balance'


# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
