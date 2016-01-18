import random
squares = []

for value in range(1,24):
	squares.append(value**2)
	

for square_value in squares:
	print(square_value)



print(squares)


def randomList(a):
	b = []
	for i in range(len(a)):
		element = random.choice(a)
		a.remove(element)	
		b.append(element)
	
	return b


squares = randomList(squares)
print("random square list")
print(squares)

print("items 1:4")
print(squares[1:4])
print("squares [0:10:2]")
for square in squares[0:10:2]:
	print(square)

print(max(squares))
print(min(squares))
print(sum(squares))





