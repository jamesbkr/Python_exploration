# THIS FILE CONTAINS EXAMPLES OF THE FUNCTIONS:
# append(), insert(), pop(), remove()

names = ['tom','jeff','tony','gary','flesher']

for name in names:
	print (name.title() + " is a wierd person.")
	
	
print(names)

#append adds to the end
names.append('frank')
print(names)	

# insert puts it where ever you specify.
#if you specify past the last element it puts it last

names.insert(4,'HERE')
print(names)

# pop() removes the last element in the list 
# It then lets you assign it
# if pop() is passed an integer value it will
# 'pop' the item at that location


popped_name = names.pop()
print(popped_name)
print(names)

# remove an item by a specific value

names.remove('jeff')
print(names)

