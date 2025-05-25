for i in range(2):
 	value = int(input('Enter an integer (-1 to break): '))
 	print('You entered:', value)
if value == -1:
	print('invalid')
else:
  print('The loop terminated without executing the break')