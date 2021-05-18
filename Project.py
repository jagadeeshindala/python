#Rock paper scissors game with computer

import random
#Function
def game(a,b):
	if(a == b):
		return None
	if(a=="r"):
		if(b=="s"):
			return False
		else:
			return True
	if(a=="s"):
		if(b=="p"):
			return False
		else:
			return True
	if(a=="p"):
		if(b=="w"):
			return False
		else:
			return True

#Driver code 
n = random.randint(1,3)
if(n == 1):
	comp = 'r'
if(n == 2):
	comp = 'p'
if(n == 3):
	comp = 's'
chr = input("Enter your choice: Rock(r) Paper(p) Scissors(s): ")
# ch = random.randint(1,3)
# if(ch == 1) :
# 	chr = 'r'
# if(ch == 2):
# 	chr = 'p'
# if(ch == 3):
# 	chr = 's'
winner = game(comp,chr)
print(f"computer choose {comp}")
print(f"You choose {chr}")
if(winner == None):
	print("The game is tied !")
elif(winner):
	print("Hurray! You Won")
else:
	print("Better luck next time")