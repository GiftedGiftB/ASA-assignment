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


for value in enumerate(cart):
	print(value)

print(list(enumerate(cart))[4])

scores.append(99)
scores.pop(1)
cart[4].insert(0, 6)
scores.extend([34,67,87,65])
print(scores)
print(cart[0].upper())
new_list = cart * 3
new_list = cart + scores
print(scores[-2])
print(scores[0:3])

print(scores[0:5:2])
#or
print(scores[::2])

