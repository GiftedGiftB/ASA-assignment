#prompt the user to enter pincipal amount
#prompt the user to enter the annual interest rate
#prompt the user to enter the duration of mortage in years 
#After prompting the user, divide annual interest rate by 100 and by 12 
#multiply duration in years by 12
#use the formula which is m= p r(1+r)^n / (1 + r)^n -1 

loan = int(input("Enter amount to be borrowed: "))

annual = int(input("Enter the annual interest rate: "))

durationofmortage = int(input("Duration of mortage in years: "))


annual = annual / 100 / 12

durationofmortage = durationofmortage * 12

calculation_1 = loan * annual * pow(1 + annual, durationofmortage)
calculation_2 = pow(1 + annual, durationofmortage) - 1

monthlypayment = calculation_1 / calculation_2

monthlypayment_roundup = round(monthlypayment, 2)

print('Your monthly payment is ', monthlypayment_roundup)
 
