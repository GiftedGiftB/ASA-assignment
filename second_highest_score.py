number_of_student = int(input('Enter number of student: '))
highest_student_name = ''
highest_student_score = 0
second_highest_student_name = ''
secocnd_highest_student_score = 0

for count in range(0,number_of_student):
	name_of_student = input('Enter student name: ')
	student_score = int(input('Enter student score: '))

if student_score > highest_student_score:
	highest_student_name = name_of_student
	highest_student_score = student_score
	second_highest_student_name = name_of_student
	secocnd_highest_student_score = student_score
	

print (f'The name of student with the highest score is {highest_student_name} with the highest score of {highest_student_score} and the second highest score goes to {second_highest_student_name} with the score of {secocnd_highest_student_score}')