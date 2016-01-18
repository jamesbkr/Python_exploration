people = ["president","boss","manager","frank","quincy","herro"]

for person in people:
	if person == "president":
		print("found the president")
	elif person == "manager":
		print("found the manager")
	else:
		print("not the president")
		
	


if "herro" not in people:
	print("not in")
elif "boss" in people:
	print("the boss is here")
	
	
if not people:
	print("no ones here")
	
if people:
	print("there is some one here")


