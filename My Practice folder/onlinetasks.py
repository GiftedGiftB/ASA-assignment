	# number 1
def greet_user(name):
	return "Hello" + name


	# number 2
def add_number(num1, num2):
	sum = num1 + num2
	return sum


	# number 3
def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False

	
	#number 4
def find_max(num1, num2, num3):
	max = num1
	if num2 > max:
		max = num2
	if num3 > max:
		max = num3
	return max




	# number 1
out_put = greet_user(" gift")
print(out_put)


	# number 2
num1 = 4
num2 = 5
sum = print(add_number(num1, num2))


	# number 3
number = is_even(10)
print(number)

	# number 4
num1 = 3
num2 = 7
num3 = 2
result = find_max(num1, num2, num3)
print(result)




