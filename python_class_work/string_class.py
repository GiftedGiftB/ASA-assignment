
text = "lion king"

#center alignment
print(f'[{text:^15}]')
print(len(f'[{text:^15}]'))

#left alignment
print(f'[{text:>15}]')
print(len(f'[{text:>15}]'))

#Right alignment
print(f'[{text:<15}]')
print(len(f'[{text:<15}]'))


num1 = 567
num2 = 39.980

print('{:d} \t {:.2f} '. format(num1, num2))

fruit = 'banana'
print(fruit*2)

fruit = 'banana for food'
print('-'.join(fruit))

#join
fruit = ['banana', 'for', 'food']
print('-'.join(fruit))

#strip

#place = 'jungle, race, on'
place = ' \t\t jungle \t\t'
print(place.strip(' '))

#turn characters to capial letter
name = 'chief okafor'
print(name.upper())

#turn characters to small letter
name = 'CHIEF OKAFOR'
print(name.lower())

#turn first letter to capital letter
name = 'chief okafor'
print(name.title())

print('car' < 'cat')
print('car' < 'cat')
print('car' == 'cat')
print('car' != 'cat')

word = 'polymorphism'
print(word.find('morph'))
print(word.index('morph'))

#split
word = "Time bound"
print(word.split())
print("-".join(word.split()))


#
raw_str = r"c:\Users\Name"
print(raw_str)

import re

pattern = '02935'
print(True if re.search(pattern,'02935') else False)

#
text = "abc123xyz"
s = re.sub(r"\d+","-",text)
print(s)

#replacing
pattern = 'yahoo.com'
text = 'gift@yahoo.com'
replacement = 'gmail.com'

result = re.sub(pattern, replacement, text)
print(result)

text = "letter story comprehension"
pattern = ' '
print(re.split(pattern, text))
