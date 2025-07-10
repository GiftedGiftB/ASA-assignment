below_number = 1
counter = 900
pi = 0.0
alternate = 1.0

for number in range(counter):
	factorial = 4.0 / below_number * alternate
	pi += factorial
	alternate *= -1
	below_number += 2
print("The summing at 10th term is: ", factorial)