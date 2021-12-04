# Import stuff here
import time
import math
# main body
print("Text Adventure")
time.sleep(1)
username = input("What is your name?: ")
charname = input("What do you want to call your character, " + username + "?: ")
time.sleep(.25)
#first room
def startingroom():
        print("We begin our journey as " + charname + " wakes up from their sleep.")
        print("They don't know it yet, but something's wrong in the kingdom.")
        input("Press [Enter] to get up.")
        print(charname + " gets up. They have a headache.")
        print(charname + " thinks that the bed is comfy, but also wants to find something to get rid of the headache")
		startingroomchoice1()
#first choice in first room
 def startingroomchoice1():
		choice = input("What do they do?: ")
        if choice == "lie down" or choice == "Go to bed":
        	print(charname + " goes back to bed. they fall asleep.")
        	startingroom()
        elif choice == "look around" or choice == "look":
        	print("Looking around reveals a bottle of advil and a glass of water on the bed stand")
		else:
			print("Sorry, I don't understand. Try 'lie down' or' look around'")
			startingroomchoice1()
# code runs here
startingroom()