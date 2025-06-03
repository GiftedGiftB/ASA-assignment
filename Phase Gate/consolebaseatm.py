print("""
		Welcome to Semicolon Bank ATM
""")
def account_balance():
	print(f"your balance is ${balance:.2f}")

def withdraw():
	amount = float(input("Enter withdrawal amount: "))
	if amount < 0:
		print("invalid withdraw amount")
	else:
		return amount
def maximum_amount():
	if amount > 20000:
		print("Twenty thousand naira per transaction")

History = []

fixed_charges = 100

balance = float(input("Enter amount: "))


is_running = True

while is_running:
	print("""
1. Account balance
2. Withdraw
3. Exit
""")
	user_number = int(input("Enter a number from 1 - 3: "))
	match user_number:
		case 1:
			account_balance()
		case 2: 
			balance = balance - withdraw()
			History.append(balance)
		case 3:
			is_running = False
		case _:
			print("invalid.")
print("Thanks for using our services")
print(History)




