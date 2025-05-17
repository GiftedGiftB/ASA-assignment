pass_and_fail= int(input('Enter result (1 = pass, 2 = fail): '))
passes = 0
failure = 0

for student in range (0, pass_and_fail):
	if pass_and_fail < 1 and pass_and_fail > 2:
		print('invalid number')
		failure += 1
	else: 
		passes += 1	

print('passed:', passes)
print('failed:', failure)