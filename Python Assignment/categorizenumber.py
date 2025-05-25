total = 0

for number in range(1,4):
	userNumber = int(input("Enter a number: "))

	divisible_number = userNumber % 5

	total += divisible_number

	if divisible_number % 5 == 0:
			 print(divisible_number)
	else:
			print("No divisible number found")
	