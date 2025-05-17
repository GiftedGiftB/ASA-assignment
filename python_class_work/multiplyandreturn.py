user_number1 = int(input("Enter first number: "))
user_number2 = int(input("Enter second number: "))

def multiply(number1, number2):
	result = 0
	for number in range(0,number2):
		result = result + number1
	return result
print(multiply(user_number1,user_number2))