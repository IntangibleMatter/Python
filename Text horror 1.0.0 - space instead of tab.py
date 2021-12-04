import time
import random

usename = input("What is your name?: ")
print("You hear a child crying")
time.sleep("You approach the child")


#debug method
def debug():
    print("")
    print("Numdebug: " + str(randnum))
    print("Turns: " + str(turns))
    print("")

#declaring/establishing the randnum and turns variables
randnum = 7

turns = 0

lastnum = 102

#Do forever
while 1 != 2:
    time.sleep(0.5)
    
    #Establishes ne random number
    randnum = random.randrange(0, 11)
    
    #Stops immediate repetition
    if randnum == lastnum:
        randnum = 10 - lastnum

    # do you do the debug method?
    if str.lower(usename) == "debug":
        debug()
    
    #this'll happen no matter what

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
    print("")
    turns = turns + 1


