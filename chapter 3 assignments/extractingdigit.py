user_number = int(input("Enter number between 1 and 10,000: "))

sum = 0
divided_number = 0

while user_number != 0:
	
	divided_number = user_number % 10
	user_number = user_number // 10
	
	sum = sum + divided_number 

print(sum)
