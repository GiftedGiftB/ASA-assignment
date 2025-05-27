import random

print("Lets play a guessing game")

random_integer = random.randint(1, 1000 + 1)
print(random_integer)

user_guess_number = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
while user_guess_number != -1:
	
	if  random_integer == user_guess_number:
		print("Congratulations. You guessed the number")
		user_guess_number = int(input("Guess a number between 1 - 1000 OR -1 to exit: "))
		if user_guess_number == -1:
			break
		elif user_guess_number != -1:
			random_integer = random.randint(1, 1000 + 1)
			print(random_integer)
			user_guess_number = int(input("Guess a number between 1 - 1000 OR -1 to exit: "))
			
	elif user_guess_number > random_integer:
		print("Too high. Try again")
		user_guess_number = int(input("Guess a number between 1 - 1000 OR -1 to exit: "))

	elif user_guess_number <  random_integer:
		print("Too low. Try again")
		user_guess_number = int(input("Guess a number between 1 - 1000 OR -1 to exit: "))

	else:
		print("invalid guess")