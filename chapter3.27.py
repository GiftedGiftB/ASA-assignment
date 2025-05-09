world_population_growth = float(input('Enter world population growth: '))

growth_rate = float(input('Enter growth rate: '))

population_growth = world_population_growth / 100
print('years\texpected world_population_growth\tnumerical increase')

for count in range (101):

	world_population1 = world_population_growth*((growth_rate)**count)

	world_population2 =
	print(count,'\t', world_population1,'\t', )
