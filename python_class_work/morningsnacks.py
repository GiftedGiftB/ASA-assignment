# number 1
nums = [10, 20, 30, 40, 50]
print(nums[3])

# number 2
list_of_colors = ['red', 'green', 'blue']
list_of_colors[2] = 'yellow'
print(list_of_colors)

# number 3
list_of_colors.append('purple')
print(list_of_colors)

# number 4
list= [1, 2, 3, 4, 5]
list.remove(3)
print(list)

# number 5
new_name = []
name_in_list = ['Alice', 'Bob', 'Charlie']
for name in name_in_list:
new_name.append(name)
    print(new_name)

# number 6
list_nums = [4, 1, 3, 9, 2]
list_nums.sort()
print(list_nums)

# number 7
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def list_of_even_numbers(list_of_numbers):
    for numbers in list_of_numbers:
        if numbers % 2 == 0:
            new_number.append(numbers)
            #print(numbers)
            return numbers







print(list_of_even_numbers(list_of_numbers))