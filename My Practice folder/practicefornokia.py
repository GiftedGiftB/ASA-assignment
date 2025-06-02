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
	menu = int(input("Enter a number: "))
	if menu == 0:
		break
	elif menu == 1 :

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
""")
	options = int(input("Enter a number: "))
	if options == 8:
		print("""
	1. Type of view
	2. Memory status
	0. Back to menu
""")
	elif menu == 2:
		print("""
		message

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
	message_setting = int(input("Enter a number: "))
	if message_setting == 7:
		print("""
	1. set
	2. common
	0. Back to menu2
""")
	set = int(input("Enter a number: "))
	if set == 1:
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
