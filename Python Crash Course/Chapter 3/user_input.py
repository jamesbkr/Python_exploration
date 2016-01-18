
#input returns a string not an int so make sure to convert numbers before using when using input

value = input("what value do you want to use\n")

print(value)


#control while loops with numerical iterators, flags. or break.

#while i<5:
	#i+=1
#while task:
	#if x: 
		#task= False
#while True:
	#if x:
		#break
		
#continue breaks a loop and starts at the begining of it again
# while X:
#	do this.......
#   if x : 
#		continue
# if the continue is not hit do the rest of this.  If the
# contue is hit then all of this will not get done.


confirmed = []
unconfirmed=['hank','frank','john','gary','tom']


# do until the data structure is empty
while unconfirmed:
	newname = unconfirmed.pop()
	print(newname)
	confirmed.append(newname)
	
print(confirmed)



# remove an instance of an object in a list
while 'hank' in confirmed:
	confirmed.remove('hank')
	
print(confirmed)	

name = input("please enter your name \n")
response = input("please enter a statement \n")
names = {}

names[name] = response

print(names)
