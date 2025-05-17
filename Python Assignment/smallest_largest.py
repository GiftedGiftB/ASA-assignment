# smallest and largest

user_number1 = int(input('Enter first number: '))

user_number2 = int(input('Enter second number: '))

user_number3 = int(input('Enter third number: '))



sum = (int(user_number1 + user_number2 + user_number3))


average = (float(sum / 3))


product = (int(user_number1 * user_number2 * user_number3))

maximum_number = max(user_number1, user_number2, user_number3)

minimum_number = min(user_number1, user_number2, user_number3)


print('The sum is: ', sum)

print('The average is: ', average)

print('The product is: ', product)

print('The maximum number is:', maximum_number)

print('The minimum number is:', minimum_number)
