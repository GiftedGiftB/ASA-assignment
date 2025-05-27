print("""
1. Create an account
2. Deposit funds into account
3. Withdraw money
0. Exit
""")
Menu = True
while Menu:
	userChoice = int(input("Select a number: "))
	if userChoice == 0:
		main_menu = False
	elif userChoice == 1:
		Name = input("Enter your name: ")
		Account_number = int(input("Enter Account Number: "))
		Password = int(input("Enter password: "))
	elif userChoice == 2:
		Name = input("Enter your name: ")
		Account_number = int(input("Enter Account Number: "))

		Menu = False
		break
	else:
		print("Invalid.Try again")
	