class BankAccount:
    def _init_(self, f_name, l_name, balance) :
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name
        self.balance = balance
        self.inv = []
        self.setup()


     def setup(self):
         print('You have create an account for {}.'.format(self.full_name))

    def deposit()
        self.balance -= amount
        print()


class AltBankAcount(BankAccount):

    def withdrawn(self, amount):
        if self.balance -amount - 200 >= 0:
            self.balance -= amount
            print('You took out {}, your balance is {}.'.format(amount, self.balance))
        else:
            print('Not enough cash :(')


account1 = BankAccount('chris', 'Jones', 60)
account2 = BankAccount('No', 'Name', 5000)


print(account1.balance)
print(account2.balance)

account2.deposit(50)
account2.withdrawn(4850)



