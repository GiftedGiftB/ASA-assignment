gallon_used = 0
miles_driven = 0
miles_per_gallon = 0
overall_average_miles = 0

while gallon_used != -1:
	gallon_used = float(input('Enter the gallons used (-1 to end): '))

	if gallon_used != -1:

		miles_driven = float(input('Enter miles driven: '))
	
		miles_per_gallon = miles_driven / gallon_used

		print('The miles/gallon for this tank was: ',miles_per_gallon)
		overall_average_miles = miles_driven / miles_per_gallon

print('The overall average miles/gallon was: ', overall_average_miles)