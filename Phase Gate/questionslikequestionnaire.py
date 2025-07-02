import random

tempNumber = 0
number = 0
times_failed = 0

for number in range(1, 3 + 1):
	minuend = random.randint(1, 100)
	subtrahend = random.randint(1, 100)

	if minuend > subtrahend:
		minuend = subtrahend
	elif minuend < subtrahend:
		tempNumber = minuend
		minuend = subtrahend 
		subtrahend = tempNumber

	total = minuend - subtrahend

	print(minuend)
	print(subtrahend)
	print(total)

	user_number = int(input("Whats the answer: "))

	if total == user_number:
		print("You are correct")

	elif total != user_number:
		print("You are wrong")
		total = minuend - subtrahend
		user_number = int(input("Whats the answer: "))

		times_failed = times_failed + 1
		
print("Total numbers of fails: ", times_failed)
print("Total number of trials: ", number)