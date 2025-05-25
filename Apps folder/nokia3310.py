main_menu = True
while main_menu:
	print("""
	   Welcome to NOKIA MENU

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
	0.Exit App
""")
	menu = int(input("Enter number: "))

	if menu == 1:
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
	menu
	options = int(input())
	if options == 8:
		print("""
	1. Type of view
	2. Memory status
""")
	elif menu == 2:
		print("""
	    Message

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
		messageSettings = int(input())
		if messageSettings == 7:
			print("""
	1. Set
	2. Common
""")
		set_option = int(input()) 
		if set_option == 1:
			print("""
		Set

	1. Message centre number
	2. Messages sent as
	3. Message validation
""")
		common = int(input())
		if common == 2:
			print("""
		Common

	1. Delivery report
	2. Reply via same center
	3. Character support
""")
	elif menu == 3:
		print("""
		Empty
""")
	elif menu == 4:
		print("""
	    Call register

	1. Missed calls
	2. Received calls
	3. Dialled numbers
	4. Erase recent call lists
	5. Show call duration
	6. Show call cost
	7. Call cost settings
	8. Prepaid  credit
""")
		showCallDuration = int(input())
		if showCallDuration == 5:
			print("""
	   Call duration

	1. Last call duration
	2. All call's duration
	3. Received calls duration
	4. Dialled calls duration
	5. Clear timers
""")
		showCallCost = int(input())
		if showCallCost == 6:
			print("""
	   Call costs
	1. Last call cost
	2. All calls cost
	3. Clear counters
""")
		showCallSettings = int(input())
		if showCallSettings == 7:
			print("""
	    Call settings
	1. Call cost limit
	2. Show costs in
""")
		PrepaidCredit = int(input())
		if PrepaidCredit == 8:
			print("""
	     Empty
""")
	elif menu == 5:
		print("""
	    Tones
	1. Ringing tone
	2. Ringing volume
	3. Incoming call alart
	4. Composer
	5. Message alartb tone
	7. Keypad tones
	8. Vibrating alart
	9. Screen saver
""")
	elif menu == 6:
		print("""
	   Settings
	1. Call settings
	2. Phone settings
	3. Security settings
	4. Restore factory settings
""")
		callSettings = int(input())
		if callSettings == 1:
			print("""
	    Call settings
	1. Automatic redial
	2. Speed dialing
	3. Call waiting options
	4. Own number sending
	5. phone line in use
	6. Automatic answer
""")
		phoneSettings = int(input())
		if phoneSettings == 2:
			print("""
	    Phone settings
	1. Language
	2. Cell info display
	3. Welcome note
	4. Network selection
	5. Lights
	6. Comfirm sim service actions
""")
		securitySettings = int(input())
		if securitySettings == 3:
			print("""
	    Security settings
	1. PIN code request
	2. Call barring service
	3. Fixed dialling
	4. Closed user group
	5. Phone security
	6. Change access codes
""")
		restoreFactory = int(input())
		if restoreFactory == 4:
			print("""
	     Empty
""")
	elif menu == 7:
		print("""
	     Emtpty
""")
	elif menu == 8:
		print("""
		Empty
""")
	elif menu == 9:
		print("""
		Empty
""")
	elif menu == 10:
		print("""
		Empty
""")
	elif menu == 11:
		print("""
	    clock
	1. Alarm clock
	2. Clock settings
	3. Date settings
	4. Stopwatch
	5. Countdown timer
	6. Auto update of date and time
""")
	elif menu == 12:
		print("""
		Empty
""")
	elif menu == 13:
		print("""
		Empty
""")
	elif menu == 0:
		main_menu = False
		break
	else:print("Invalid.Try again")