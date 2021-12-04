from random import randint #Import the random integer generator

hexlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'] #Every hex digit

def pickcolour(level, string, alpha): #Define the pickcolour function with the arguments for how many times it's gone through, what the colour is so far, and whether to have an alpha value in the string
    if level == 0: #First go around
        level += 1 #Increase level by one so we don't run this if block again
        if alpha == 'y': #If we are including alpha, we need to add an FF to the beginning of the colour
            string += hexlist[-1] + hexlist[-1] #Add FF to the beginning of the colour
    elif level < 7: # If the colour isn't complete, do this
        string += hexlist[randint(0, 15)] #Add a random hex value to the colour
        level += 1 #Increment level by one so we don't end up in an unescaped recursive loop
    else: #Do for final recursion
        return string #Return the colour
    return(pickcolour(level, string, alpha)) #This line is where everything comes flooding back at the end

def colourpicker(): #Define the function colourpicker
    amount = int(input("How many colours do you want in your pallette? ")) #Get an integer of how many colours you want in the palette
    showalpha = input("Would you like the colour codes to start with an aplha (transparency) value? (y/n) ").lower() #Get whether the user wants an alpha value
    sort = input("Would you like the colours to be sorted? (y/n) ").lower() #Get whether the user wants the colours to be sorted
    colours = [] #Define the array of colours as empty
    if showalpha == 'y': #If an alpha value was wanted do this code block
        print("Format: AARRGGBB") #Explains the format of the colour - 2 alpha, 2 red, 2 green, 2 blue
    else: #If an alpha value wasn't wanted, or if it was unclear, do this code block
        print("Format: RRGGBB") #Explains the format of the colour - 2 red, 2 green, 2 blue
    
    i = 0 #Variable that makes sure the next block only runs as many times as needed
    while i < amount: #While we don't have as many colours as wanted run this block
        colours.append(pickcolour(0, "", showalpha)) #Add the new colour to the list of colours
        i += 1 #Add one to the escape value so we don't run forever
    print("Sorted:") #Makes sure the user knows the list of colours is sorted

    if sort == "y": #Run this block if we want the colours to be sorted
        colours.sort() #Sort the colours... alphabetically
        for n in colours: #While we haven't printed out every colour in the list, run this code
            print(n) #Print out a colour from the list
    else: #Run this if we don't want the colours sorted, o if we don't know whether we want the colours sorted
        for n in colours: #While we haven't printed out every colour in the list, run this code
            print(n) #Print out a colour from the list
    
    if input("pick more colours? (y/n) ").lower() == 'y': #If the user wants more colours, do this block
        colourpicker() #Run the function again
    else: #If the user doesn't want more colours, or if it was unclear, do this block
        return 0 #End the program

colourpicker() #Run the colourpicker function

