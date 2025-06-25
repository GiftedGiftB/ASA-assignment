class Account:

	#def __init__(self, name = "",  balance = 0):
    def __init__(self):
        #self.name = name
        self.balance = 0

    def withdraw(self):
        print('Acount withdraw')

    def deposit(self, amount):
        #print('Account deposit')
        self.balance += amount




oba = Account()
print(oba.balance)
#oba.withdraw()
oba.deposit(1000)
print(oba.balance)