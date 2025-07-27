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

print() # 14
numbers = [10, 15, 20, 25, 30]

#numbers.append(18)
numbers.insert(2, 18)
print(numbers)


print()  #15
def greet_user(name):
	print("hello," + name)

greet_user("gift!")

print()  #16
def add_numbers(num1, num2):
	sum = num1 + num2
	return sum

sum = print(add_numbers(8, 12))


print()  #17
def get_first_item(lists):
	return lists[0]


lists = get_first_item(["sun", "moon", "stars"])
print(lists)


print()  #18
def count_even_numbers(list):
	count = 0
	for numbers in list:
		if numbers % 2 == 0:
			count += 1
	return count

result = count_even_numbers([2, 5, 8, 11, 14, 17])
print(result)


print()   #19

def reverse_list(list):
	return list[::-1]

result = reverse_list([1, 2, 3, 4, 5])
print(result)

restore_list = reverse_list(result)
print(restore_list)

