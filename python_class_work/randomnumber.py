import random
list = []

def random_number():

    for numbers in range (1, 10 + 1):
        random_number = random.randint(1, 50)
        list.append(random_number)

    print(list)

def get_length(number):
   count = 0
   #for numbers in range (number):

random_number()