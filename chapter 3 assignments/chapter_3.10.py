annual_rate_return= 7/100
amount_invested = 1000
total_amount = 0

for number in range(1, 31):
	
	amount_on_deposit = amount_invested * (1 + annual_rate_return) ** number

	total_amount = round(amount_on_deposit, 2)

	print(f'The amount of money you will have at the end of: {number} year is: ${total_amount:,.2f}')



	
