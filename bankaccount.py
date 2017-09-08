class BankAccount:
    def _init_(self, f_name, l_name, balance) :
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name
        self.balance = balance
        self.inv = []
        self.setup()


     def setup(self) :
         print('You have create an account for {}.'.format(self.full_name

account1 = BankAccount('chris', 'Jones', 60)
account2 = BankAccount('No Name', 5000)


account1.name = 'chris'
account2.name = 'joe'

print(account1.name)
print(account2.name)
