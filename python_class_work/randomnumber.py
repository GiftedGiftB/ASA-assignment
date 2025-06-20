import random
list = []

def random_number():
    for numbers in range (1, 10 + 1):
        random_number = random.randint(1, 50)
        list.append(random_number)

    print("the random number is: ", list)

def get_length(list):
   count = 0
   for i in list:
       count += 1
   print("length of list is: ", count)
   return count


def get_even_positions(list):
    sum = 0
    count = 0
    for numbers in list:
        if count % 2 == 0:
            sum += numbers
        count += 1
    print("sum of element at even position is: ", sum)
    return sum

def get_odd_positions(list):
    sum = 0
    count = 0
    for numbers in list:
        if count % 2 == 1:
            sum += numbers
        count += 1
    print("sum of element at odd position is: ", sum)
    return sum

def get_element_at_every_third_position(list):
    sum = 1
    count = 1
    for numbers in list:
        if count % 3 == 0:
            sum *= numbers
        count += 1
    print("multiplication of element at third positions is: ", sum)
    return sum

def get_average(list):
    sum = 0
    average = 0
    count = 0
    for numbers in list:
        count += 1
        sum += numbers
        average = sum / count
    print("average is: ", average)
    return average








random_number()
get_length(list)
get_even_positions(list)
get_odd_positions(list)
get_element_at_every_third_position(list)
get_average(list)