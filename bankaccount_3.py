class BankAccount:
    def __init__(self, f_name, l_name, balance):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name
        self.balance = balance
        self.setup()

    def setup(self):
        print('You have create an account for {}.'.format(self.full_name))

account1 = BankAccount('Chris', 'Jones',60)
account2 = BankAccount('No', 'Name',5000)


