investment_amount = int(input('Enter investment amount: '))

number_of_year = int(input('Enter number of years: '))

interest_rate = int(input('Enter interest rate: '))

interest_rate = interest_rate / 100

for number in range (1,number_of_year + 1):

	interest = investment_amount * (1 + interest_rate )** number
	
	#sum = intrest + investment_amount 

	print(f'your investment for year:{number} is:{interest:,.2f}')