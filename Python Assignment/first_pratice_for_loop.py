#for number in range (0, 11, 2):

	#print(number, end = '\t')

total_score = 0
for number in range (10):
	score = int(input('Enter score: '))
	total_score += score

average = total_score / 10

print(f'The total is: {total_score} and the average is:{average} ')
