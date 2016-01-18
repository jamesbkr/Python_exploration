
# remember dictionaries have no order and maintain no order.  Use them when order in not important.

heroes = {'Super Man' : 1, 'Batman': 2, 'Joker': 3,'Ant Man':4,'Cat Women':5}

for hero in heroes:
	print(heroes[hero])
	

heroes['Gotham'] = 6
	
print(heroes)

del heroes['Gotham']

print(heroes)

# this is the for loop construction to loop throught the key value pairs
for name,score in heroes.items():
	print(name + "  " + str(score))

for key,value in heroes.items():
	print(key + "  " +str(value))
	
for value in heroes.keys():
	print(value)
