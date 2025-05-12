amount_invested = 1000
annual_rate_return= 7/100
year1 = 10
year2 = 20
year3 = 30
amount_on_deposit = 0

amount_on_deposit = amount_invested * (1 + annual_rate_return) ** 10

amount_on_deposit1 = round(amount_on_deposit, 2)

print('In 10 years you will have: ', '$', amount_on_deposit1)



amount_on_deposit = amount_invested * (1 + annual_rate_return) ** 20

amount_on_deposit1 = round(amount_on_deposit, 2)

print('In 20 years you will have: ', '$', amount_on_deposit1)



amount_on_deposit = amount_invested * (1 + annual_rate_return) ** 30

amount_on_deposit1 = round(amount_on_deposit, 2)

print('In 30 years you will have: ', '$', amount_on_deposit1)