passes = 0
failure = 0

for student in range (10):
	result = int(input('Enter result (1 = pass, 2 = fail): '))
	if result < 0 and result > 2:
		print('invalid number')

	if result == 1 and result == 2:
		passes = passes + 1
	else: 
		failures = failure + 1

print('passed:', passes)
print('failed:', failure)

if passes > 8:
	print('Bonus to insructor')