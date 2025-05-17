def nokia3310_menu():
	print("""
	NOKIA 3310 MENU
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
while True:
	nokia3310_menu()
	userNumber = int(input("Enter a number: "))
	match userNumber:

		case 1:
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
phone_book = int(input("Enter a number: "))

	