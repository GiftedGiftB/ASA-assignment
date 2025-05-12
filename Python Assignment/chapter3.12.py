number = int(input('Enter a five digit number: '))

if number > 99999:
	print('invalid number')

number1 = (number // 10000) % 10
number2 = (number // 1000) % 10
number3 = (number // 100) % 10
number4 = (number // 10) % 10
number5 = (number // 1) % 10

originalNumber = number1, number2, number3, number4, number5

reversedNumber = number5, number4, number3, number2, number1

if originalNumber == reversedNumber:
	print('it is a palindrome number')
else:
	print('it is not a palindrome number')