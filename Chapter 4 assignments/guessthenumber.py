import random

print("Lets play a guessing game")

random_integer = random.randint(1, 1000 + 1)
print(random_integer)

break_out = int(input("Enter a number: "))

user_guess_number = int(input("Guess a number between 1 - 1000: "))

while break_out != -1:

	if  random_integer == user_guess_number:
		print("Congratulation. you win")
	elif user_guess_number > random_integer:
		print("Too high. Try again")
	elif user_guess_number <  random_integer:
		print("Too low. Try again")
	else:
		print("invalid guess")