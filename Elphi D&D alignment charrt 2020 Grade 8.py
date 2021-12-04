import time
import random
# import only system from os 
from os import system, name

def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

multiples = ["Molly", "Ben", "Georgia", "Liam"]

name = input("What is your (First) name?: ")
name = name.lower()
name = name.capitalize()
if name in multiples:
    lname = input("Sorry, it seems there are multiple grade 8s with your name, what is the first letter of your last name?: ")
    lname = lname.capitalize()
    name = name +" " + lname

if name == "Lyric":
    print("Welcome, creator.")
#lists

#I've inputed 49 people in our grade to the lists so far

#Good lists
LG = ["Lgtest", "Fernando", "Bethany", "Niya", "Josh"]
NG = ["Ngtest", "Russell", "Sofie", "Alana" "Millie", "Lucy", "Erin", "Sydney", "Owen", "Tj", "Scott", "Esme", "Bailey", "Josie", "Cael"]
CG = ["Cgtest", "Lyric", "Demyana", "Demy", "Megan", "Quinn", "Georgia", "Sage", "Mya", "Liam M"]
#Neutral lists
LN = ["Lntest", "Samuel", "Molly C", "Sahra", "Eilis", "Dani", "Danielle", "Isabella", "Zander", "Liam N", "Kayla", "Eli", "Harris"]
TN = ["Tntest", "Hanna", "Cole", "April", "Erin", "Bryshaun", "Shaun"]
CN = ["Cntest", "Sam", "Maddy", "Molly R", "Anna", "Brinley", "Jesse", "Rowan", "Olivia", "Shelby"]
#Evil lists
LE = ["Letest", "Jäger", "Sami", "Samantha", "Bodhi"]
NE = ["Netest", ""]
CE = ["Cetest", ""]

if name == "Debug":
    print(LG)
    print(NG)
    print(CG)
    print(LN)
    print(TN)
    print(CN)
    print(LE)
    print(NE)
    print(CE)

#Get random string, just in case.
randtext = "True Neutral (TN)!"
randnum = 5
randnum = random.randint(0, 5)
if randnum == 0:
    randtext == "Neutral Good (NG)!"
elif randnum == 1:
    randtext == "Chaotic Good CG)!"
elif randnum == 2:
    randtext == "Lawful Good (LG)!"
elif randtext == 3:
    randtext == "Lawful Neutral (LN)!"
else:
    randtext = "Chaotic Neutral! (CN)"

def getalignment():
    if name in LG:
        print("Your name was found in the Lawful Good (LG) list! Impressive!")
    elif name in NG:
        print("Your name was found in the Neutral Good (NG) list! Very nice!")
    elif name in CG:
        print("Your name was found in the Chaotic Good (CG) list! Quite fun!")
    elif name in LN:
        print("Your name was found in the Lawful Neutral (LN) list! Interesting!")
    elif name in TN:
        print("Your name was found in the True Neutral (TN) list! Fascinating!")
    elif name in CN:
        print("Your name was found in the Chaotic Neutral (CN) list! Intriguing!")
    elif name in LE:
        print("Your name was found in the Lawful Evil (LE) list! Unpleasant!")
    elif name in NE:
        print("Your name was found in the Neutral Evil (NE) list! Atrocious!")
    elif name in CE:
        print("Your name was found in the Chaotic Evil (CE) list! Malevolent!")
    else:
        print("Your name wasn't found on any list! Sorry about that! I think you might be " + randtext)
getalignment()
print("Please note that this is not meant to be taken seriously, and may not even reflect the creator of this program's opinion.")
input("Press [ENTER] to exit")
