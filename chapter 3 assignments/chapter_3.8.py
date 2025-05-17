#Arithmetic, smallest and largest)

sum = 0
product = 1
largest = 0
smallest = 0

for number in range(1, 4 + 1):
	integer = int(input('Enter number: '))

	sum += integer
	average = sum / 4
	product *= integer
	
	if integer > largest:
		largest = integer

	if integer < smallest:
		smallest = integer

print('The sum is:',sum)

print('The average number  is:',average)

print('The product is:',product)

print('The largest number is:',largest)

print('The smallest number is:',smallest)