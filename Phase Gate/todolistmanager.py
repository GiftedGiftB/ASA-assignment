menu = True
while menu:
	print("""
	To-Do-List Manager
1. Add a task
2. View all tasks
3. Mark a task as complete
4. Delete a task
5. Exit

""")
	menu = int(input("Enter a number: "))

	if menu == 1:
		print("""
	Add a task

""")
	elif menu == 2:
		print("""
	View all tasks

""")
	elif menu == 3:
		print("""
	Mark a task as complete
""")
	elif menu == 4:
		print("""
	Delete a task as complete
""")
	elif menu == 5:
		print("Goodbye")
		menu = False
		break
	else:print("Invalid.Try again")
