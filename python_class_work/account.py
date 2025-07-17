class Account:

	#def __init__(self, name = "",  balance = 0):
    def __init__(self, name):
        #self.name = name
        self.balance = 0.00

    def get_name(self) :
        return self.name

    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = amount

    def get_balance(self):
        return self.balance

    def withdraw(self):
        print('Account withdraw')

    def deposit(self, amount):
        #print('Account deposit')
        self.balance += amount




oba = Account("oba")
print(oba.balance)
#oba.withdraw()
oba.deposit(1000)
print(oba.balance)