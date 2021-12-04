import json

#things to be printed in commands
h = """-h: help
-q: quit
-g: guide to using this program
-n: create new dialogue
-o: open existing dialogue file to edit
"""

g = """Style mandates:
unless you're typing what the character is saying, there should be no spaces and no capitals. use underscores, numbers, and lowercase letters ONLY.

Creating a dialogue file:
when creating a new dialogue, you will be asked two questions to start:
What is the region the game takes place in, and what you want to call the dialogue
The first is answered simply, as it just determines what area the dialogue takes place in (For example, Bowser's Castle, Waterfall, or The Nether)
Let's say for this example it's the Final Castle, so "final_castle"
The second is a little harder, but still fairly easy. Enter a title which isn't already used and helps describe what the dialogue does.
For example, if it were a dialogue where the Villain, Emma, monologued to the player you could call it "emma_monologue"
the dialogue would then be saved as "final_castle_emma_monologue.json"

Creating Dialogue:

"""

commands = {"-h": "print(h)",
            "-q": "return",
            "-g": "print(g)",
            "-n": "new_file()"}

####################
# New file process #
####################

def new_file():
    region = input("What region in the game will this take place? ")
    file_name = input("What would you like to name the dialogue file? ")
    file_name_save_as = region + file_name

    dialogue = {"region": region, "file_name": file_name}


def create_dialogue():
    pass

####################
#   Program core   #
####################

# note: Must be at end of file otherwise exec() won't work

def input_loop():
    i = input("command: ").lower()
    if i != "-q":
        check_input(i)
        input_loop()
    else:
        
        return

def check_input(i):
    if i in commands:
        exec(commands[i])
        return
    else:
        print("command not recognized. please try again. (type -h for help)")
        return

def main():
    print("Welcome to the IntangibleMatter Dialogue File Builder")
    print("Type -h for a list of commands")
    input_loop()

main()


