def create_account():
	createAccount = int(input("Enter account number: "))
	name = input("Enter name: ")

def show_balance():
	print(f"your balance is ${balance:.2f}")

def deposit():
	amount = float(input("Enter amount deposit amount: "))
	if amount < 0:
		print("invalid amount")
	else:
		return amount
def withdraw():
	amount1 = float(input("Enter withdrawal amount: "))
	if amount < 0:
		print("invalid withdraw amount")
	else:
		return amount

balance = 0
is_running = True

while is_running:
	print("""
1. Create account
2. Deposit
3. Withdraw money
4. show_balance
5. Exit
""")
	userNumber = int(input("Enter a number from 1 - 4: "))
	match userNumber:
		case 1:
			create_account()
		case 2:
			balance -= withdraw()
		case 3: 
			balance += deposit()
		case 4: 
			show_balance()
		case 5:
			is_running = False
		case _:
			print("invalid.")
print("Goodbye")



