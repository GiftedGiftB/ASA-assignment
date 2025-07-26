print()  # 1
numbers = [3, 7, 1, 9, 4]
print(numbers[2])

print()  #2
list = ["apple", "banana", "cherry", "date"]
print(list[-2])

print()  #3
list = ["red", "green", "blue", "yellow", "purple"]
print(list[1:4])

print()  #4
list = ["cat", "dog", "rabbit"]
list.append("elephant")
print(list)

print()  #5
list = [10, 20, 30, 40]
for number in list:
	print(number + 5)

print()  #6
list = ["Ali", "Zara", "Mina"]
for name in range(len(list)):
	print(f"Hello, {list[name]}")

print()  #7
list = [50, 60, 70, 80]
list[2] = 100
print(list)

print()  #8
list = [5, 12, 7, 20, 3]
for number in list:

	if number > 10:
		print(number)

print()  #9
list = [2, 4, 6, 8]
result = 0
for number in list:
	result += number
print(result)

print()  #10
list = ["Paris", "London", "Tokyo", "Dubai"]
if "Paris" in list:
	print("found")
else:
	print("not found")

print()  #11
temperatures = [22, 25, 19, 30, 28]
print(max(temperatures))
print()  # OR
temperatures = [22, 25, 19, 30, 28]
max_number = temperatures[0]

for numbers in temperatures:
	if numbers > max_number:
		max_number = numbers
print(max_number)

print()  #12
marks = [65, 70, 55, 80, 90]

sum = 0
count = 0
for number in marks:
	sum += number

for number in marks:
	count += 1
average = sum / count

print(average)

print()  # 13
letters = ['a', 'b', 'c', 'd', 'e']
letters.pop(2)
print(letters)
