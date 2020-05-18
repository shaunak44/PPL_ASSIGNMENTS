import random
min = 1
max = 6
roll_again = "Y"
while(roll_again == "Y"):
	roll_again = raw_input("roll_again[Y/n]?")
	if(roll_again == "Y"):
		print(random.randint(min, max))
	elif(roll_again == "n"):
		break
	else :
		print("Enter valid input")

