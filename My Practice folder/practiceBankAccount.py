class practiceBankAccount:
	def __init__(self, owner, balance = 0):
		self.owner = owner
		self.__balance = balance 


	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			print(f"Deposited ${amount}")
		else:
			print("Deposit amount must be positive")





account = practiceBankAccount("Alice",100)
account.deposit(50)