userNumber= int(input('Enter a five digit number: '))

if userNumber > 99999:
  print('Invalid number') 

userNumber1 = (userNumber //  10000) % 10
userNumber2 = (userNumber //  1000) % 10
userNumber3 = (userNumber //  100) % 10
userNumber4 = (userNumber //  10) % 10
userNumber5 = (userNumber //  1) % 10


print(userNumber1,   userNumber2,   userNumber3,   userNumber4,   userNumber5)