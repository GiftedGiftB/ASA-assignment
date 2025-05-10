n= int (input('Enter number: '))
for  number in range(n,0,-1): 
 print(number)
if number == 1:
 print('Blast off!')
elif number < 1:
 n= int (input('Enter number: '))
