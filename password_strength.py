user_password = int(input('Enter password not less than 8 digit: '))

if user_password < 99999999:
	print('Your password is very weak')

if user_password == 99999999:
	print('Your password is weak')

if user_password >= 99999999 and user_password <= 9999999999999999:
	print('Your password is strong')

if user_password > 1000000000000000:
	print('Your password is very strong')