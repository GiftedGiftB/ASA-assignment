scores = [50,43,67,34,56]

cart = ['banana', 33 , 'juice', 2.5, ["fish", "palm oil"], True]

print("we have", len(scores), "scores")
print(scores[0:3])
print("picking number by the index in scores: ", scores[3])
print("picking number by the index in",len(cart))
print(cart[4])


for score in scores:
	print(score)
for idx in range(len(scores)):
	print(idx)