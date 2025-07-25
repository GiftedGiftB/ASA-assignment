number = [3,7,1,9,4]
print(number[2])

fruit = ["apple", "banana", "cherry", "date"]
print(fruit[-1])

colors = ["red", "green", "blue", "yellow", "purple"]
print(colors[1:4])

animals = ["cat", "dog", "rabbit"]
animals.append("elephant")
print(animals)

numbers = [10, 20, 30, 40]
for num in numbers:
	print(num * 5)

names = ["Ali", "Zara", "Mina"]
for name in range(len(names)):
	print(f"Hello, {names[name]}!")

scores = [50, 60, 70, 80]
scores[2] = 100
print(scores)

numbers = [5, 12, 7,20, 3]
for num in numbers:
	if num > 10:
		print(num)

numbers = [2, 4, 6,8]
total = 0
for num in numbers:
	total += num
print(total)


