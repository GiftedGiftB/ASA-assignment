

loan = int(input("Enter amount to be borrowed: "))

annual = int(input("Enter the annual interest rate: "))

durationofmortage = int(input("Duration of mortage in years: "))


annual = annual / 100 / 12

durationofmortage = durationofmortage * 12

cal = loan * annual * pow(1 + annual, durationofmortage)
cal2 = pow(1 + annual, durationofmortage) - 1

monthlypayment = cal / cal2

print('Your monthly payment is ', monthlypayment)
 
