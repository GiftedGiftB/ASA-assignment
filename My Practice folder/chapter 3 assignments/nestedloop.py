n=10
for row in range(n):
	for column in range(row + 1):
		print('*', end="")

	print()

print()

n = 10
for row in range(n):
	for column in range(row,n):
		print('*',end = "")

	print() 

print()

n = 10
for row in range (n):
	for column in range(row + 1):
		print(' ',end ='') 

	for column in range(row,n):
		print('*',end = '')

	print()


print()

n = 10
for row in range(n):
	for column in range(row,n):
		print(' ',end = '')

	for column in range(row + 1):
		print('*',end = '')

	print()


