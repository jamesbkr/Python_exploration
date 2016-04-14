def greet_user():
	
	print("Hello")


greet_user()	


def pass_argument(username):
	
	print(username)
	
	
	
pass_argument("frank")

###when passing argumetns,  default values can be set.  They will be overwritten if a value
###is entered but will use default if no value is passed.
##Return value can be used in the same way as java.
## if you want to prevent a function from modifying a list, send it a slice list[:]

## this will send a copy instead of the actual list.

##to pass an arbitrary number of values to a list, use *items.

## this allows for a variable number of elements to be passed
## **items is an arbitrary number of key value pairs

