user_age = int(input('Enter your age: '))

maximum_heart_rate = 220 - user_age

target_heart_rate = (85 / 100) * maximum_heart_rate

rounded_number = round(target_heart_rate)

print('The maximum heart rate is: ', maximum_heart_rate)

print('Your target heart range is: ', rounded_number)