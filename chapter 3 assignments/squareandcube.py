print("Number\tSquare\tcube")

for number in range(0,5 + 1):
	square = number **2 
	cube = number **3
	print(f"{number:>6}\t{square:>6}\t{cube:>4}")