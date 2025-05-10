purchase_amount = int(input('Enter purchase amount: '))

if purchase_amount >= 1000 and purchase_amount <= 10000:

	discount_offered = (5 / 100) * purchase_amount
	
	price_after_discount = purchase_amount - discount_offered

	#print(f'Your discount is:%{discount_offered} and your current price is:{price_after_discount:,.2f}')


elif purchase_amount >= 10000 and purchase_amount <= 50000:

	discount_offered = (10 / 100) * purchase_amount

	#print(f'Your discount is:%{discount_offered} and your current price is:{price_after_discount:,.2f}')

elif purchase_amount > 50000:

	discount_offered = (20 / 100) * purchase_amount

print(f'Your discount is:%{discount_offered:,.2f} and your current price is:{price_after_discount:,.4f}')

