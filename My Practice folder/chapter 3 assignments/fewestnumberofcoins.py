purchase_price = float(input('Enter purchase amount in: '))
amount_purchaser_paid = float(input('Enter amount paid: '))

purchaser_change = purchase_price - amount_purchaser_paid

cent_in_change = 73

quarters = (cent_in_change / 25) % 25

dimes = (cent_in_change / 10) % 10

pennies = (cent_in_change / 1) % 1

print(f'Your change is: {quarters},{dimes} and {pennies}')