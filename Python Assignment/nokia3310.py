while True:
	print("""
		NOKIA MENU
	1.Phone book
	2.Messages
	3.Chat
	4.Call register
	5.Tones
	6.Settings
	7.Call divert
	8.Games
	9.Calculator
	10.Reminders
	11.Clock
	12.Profile
	13.Sim service
	0. Exit
	""")
	menu = int(input("Enter 0 to exit or enter number from 1 - 13: "))
	if menu == 0:
		print("Exiting app")
		break

	elif menu == 1 :
		while True:
			print("""
	     Phone book
	1.Search
	2.Service Nos
	3.Add name
	4.Erase
	5.Edit
	6.Assign tone
	7.Send b'card
	8.Options
	9.Speed
	10.Voice tags
	0. Back

	""")
	phone_book = int(input("Enter a number from 1 - 10: "))
	if phone_book == 0:
		break

	elif phone_book == 1:
		while True:
			print("""
		Search
	0. Back
	""")

	elif phone_book == 2:
			while True:
				print("""
		Service Nos
	0. Back
	""")
	elif phone_book == 3:
		while True:
			print("""
		Add name
	0. Back
	""")
	elif phone_book == 4:
		while True:
			print("""
		Errase
	0. Back
	""")
	elif phone_book == 5:
		while True:
			print("""
		Edit
	0. Back
	""")
	elif phone_book == 6:
		while True:
			print("""
		Assign Tone
	0. Back
	""")
	elif phone_book == 7:
		while True:
			print("""
		Send B Card
	0. Back
	""")
	elif phone_book == 8:
		print("""
		Options
	1. Type of view
	2. Memory status
	0. Back to menu
	""")
	elif phone_book == 9:
		while True:
			print("""
		Speed Dials
	0. Back
	""")
	elif phone_book == 10:
		while True:
			print("""
		Voice Tags
	0. Back
	""")
	else:
		print("invalid")
		break

	menu = int(input("Enter 0 to exit or enter number from 1 - 13: "))
	if menu == 0:
		print("Exiting app")
		break

	elif menu == 2:
			while True:
				print("""
		Messages
	1. Write messages
	2. Inbox 
	3. Outbox
	4. Picture messages
	5. Tempates
	6. Smileys
	7. Message settings
	8. Info service
	9. Voice mailbox number
	10. Service command editor 
	""")
	messgae = int(input("Enter a number from 1 - 10: "))
	if message == 1 or message == 2 or message == 3 or message == 4 or message == 5 or message == 6 or message == 8 or message == 9 or message == 10:
		print("0. Back")
	elif massage == 7:
		print("""
		Message settings
	1. set
	2. common
	0. Back to menu2
""")
	Message_settings = int(input("Enter a number from 0 - 2: "))
	if Message_settings == 1:
		print("""
		set
	1. Message centre number
	2. Messages sent as
	3. Message validation
""")
	elif set == 2:
		print("""
		common

	1. Delivery report
	2. Reply via same center
	3. Character support
""")
	menu = int(input("Enter a number: "))
	System.out.print("""
		Empty

""")