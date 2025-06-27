number = [4,55,43,32,65]
# to sort
number.sort()
print("arange number: ", number)

# to remove with the index number
number.pop(3)
print("remove index: ", number)

# to add
number.append(21)
print("add number: ", number)

# to remove the value
number.remove(32)
print("remove number: ", number)

#
length = len(number)
for i in range(length):
    print(number[i])
