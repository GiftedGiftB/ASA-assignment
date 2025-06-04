print("  Welcome to semicolon Employees payroll ")

History = []

#for people in History

def employees_details():
	History.append(name)
	History.append(hour_worked)
	History.append(pay_rate)
	History.append(fedral_tax)
	History.append(state_tax)
	
def view_details():
	print(History)

#def update_details():
	print(History)

is_running = True

while is_running:
	print("""
1. Add Employees payroll
2. View Employees payroll
3. Update Employees payroll
4. Exit
""")
	employer = int(input("Enter number: "))
	match employer:
		case 1:
			name = input("Enter name of employee: ")

			hours_worked = int(input("Enter number of hours worked: "))

			pay_rate = int(input("Enter Hourly pay rate: "))

			fedral_tax = int(input("Enter fedral tax withholding rate: "))	
			state_tax = int(input("Enter state tax withholding rate: "))
			
		case 2:
			view_details()
		case 3:
			update_details()
		case 4:
			is_running = False
		case _:
			print("invalid")

print("Thanks for using our App")



