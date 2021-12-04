import time
import random
usename = input("What is your name?: ")

def newrandnum(num1, num2):
	randnum = random.randrange(num1, num2)

def debug():
	print("Numdebug: " + str(randnum))
	print("Turns: " + str(turns))

turns = 0
while 1 != 2:
	time.sleep(0.5)
	
	randnum = 7
	
	lastnum = 102
	
	newrandnum(0, 11)
	
	if randnum == lastnum:
		newrandnum(0, 11)
	
	if str.lower(usename) == "debug":
		debug()
	
	if randnum != -1:
		if randnum == 0:
			print("Help")
		elif randnum == 1: 
			print("Help me")
		elif randnum == 2:
			print("It hurts so much")
		elif randnum == 3:
			print("Save me, " + usename)
		elif randnum == 4:
			print("Why can't you help me, " + usename)
		elif randnum == 5:
			print(usename + "...")
		elif randnum == 6:
			print("Why won't the pain stop, " + usename + "?")
		elif randnum == 7:
			print("MAKE IT STOP, " + str.upper(usename) + " MAKE IT STOP!")
		elif randnum == 8:
			print("...")
		elif randnum == 9:
			print("Why won't it end?")
		else:
			print(str.upper(usename))
			
	lastnum = randnum
	time.sleep(0.5)
	
	input("How do you respond?: ")
	turns = turns + 1

