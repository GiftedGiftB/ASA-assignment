# factorials
 
factorial_number = int(input('Enter a nonnegative number: '))

total = 1

for number in range(factorial_number,0,-1):

	total *= number

print('The factorial of the number you entered is: ',total)
