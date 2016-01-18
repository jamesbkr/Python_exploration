# function sample code.

# define a function

import functions_import
# to import specific functions
#  --> from functions_import import function_1


def function_name(integer_value):
	print("function call")
	print(integer_value)
	return integer_value + 1
# call function

return_value=function_name(integer_value = 4)
print(return_value)


# to pass a copy of a list not the actual list
# function_name(names[:])

# pass an arbitraty number of arguments to a function
# *toppings



functions_import.function_1()
functions_import.function_2()
