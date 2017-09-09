class BankAccount:
    def __init__(self, f_name, l_name, balance=0):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name
        self.balance = balance
        self.inv = []
        self.setup()

    def deposit(self, amount):
        self.balance += amount
        print('you deposit {} your new balance is {}.'.format(amount, self.balance))

    def setup(self):
        print('You have create an account for {}.'.format(self.full_name))

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print('You took out {}, your balance is {}.'.format(amount, self.balance))
        else:
            print('Not enough cash :(')

    # def __str__(self):
    #     return 'Account of {}.'.format(self.full_name)

    def __repr__(self):
        return self.__str__()


class AltBankAccount(BankAccount):
    def withdraw(self, amount, cancel=False):
        if cancel:
            return super().withdraw(amount)
        elif self.balance - amount - 200 >= 0:
            self.balance -= amount
            print('You took out {}, your balance is {}.'.format(amount, self.balance))
        else:
            print('Not enough cash :(')


account1 = BankAccount('Chris', 'Jones', 60)
account2 = AltBankAccount('No', 'Name', 5000)

# print(account1.balance)
# print(account2.balance)

print(account2)

# account2.withdraw(5050)
