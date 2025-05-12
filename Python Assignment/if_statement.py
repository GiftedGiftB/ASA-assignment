score = input("Enter student score: ")
if type (score) == int:
	if score > '49':
		print('you pass')
		print('your score is: ',score)
	else:
		print('you failed')
		print('your score is: ', score)
else:
	print('invalid type')