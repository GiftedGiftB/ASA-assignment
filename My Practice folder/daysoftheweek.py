date = 0
while date != -1:
	date = int(input('Enter the date 1 - 7: '))

	match date:
		case 1:
			print('monday')
		case 2:
			print('tuesday')
		case 3:
			print('wednesday')
		case 4:
			print('thursday')
		case 5: 
			print('friday') 
		case 6:
			print('saturday')
		case 7:
			print('sunday')
		case default:
			print('invalid')
		