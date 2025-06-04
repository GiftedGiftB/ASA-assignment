def get_product(*arg):
        product = 1
        for digits in arg:
                product = product * arg 
        return product

result = get_product(5, 4)
print(result)

total = get_product(12, 2, 3, 13, 15)
print(total)