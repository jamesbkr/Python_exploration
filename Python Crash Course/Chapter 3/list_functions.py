# THIS FILE CONTAINS EXAMPLES OF:
# sort()


#sort() perminantly changes the order of the list according to the data type
cars = ['honda','ferari','toyota','ducati']
cars.sort()
print(cars)

#sort(reverse=True) prints list backwards
cars.sort(reverse=True)
print(cars)


# sorted does not alter the list but returns a sorted version of it
print(sorted(cars))
print(cars)
#reverse() reverses the order of the list

cars.reverse()
print(cars)

#len() finds the length of a list

print(len(cars))
