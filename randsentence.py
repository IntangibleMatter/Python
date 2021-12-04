#Random sentence generator

#Import things for code
from time import sleep

from random import randint

#See if a devcode is added, and act as a buffer
type = input("Press enter to start ")

#Lists
Names = ["Linda", "Griffynn", "Cole", "Ailie", "TJ", "Millie", "Preston", "Danielle", "Demyana", "Lilly", "Theresa", "Tyson", "Jennifer", "Renee", "Jaidon", "Lyric", "Ian", "Eilis", "Bryshaun", "Molly", "Jager", "Sahra", "Georgia", "Yael", "Ben", "Sylvia", "brown fox", "dog"]

Adjectives = ["rainbow", "non-binary", "fucking", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "sparkly", "lazy", "Canadian", "Caucasian", "African", "Asian", "Native", "bright", "redundant", "cubic", "drab", "soft", "quaint", "shiny", "long", "tame", "bonkers"]

Adverbs = ["abruptly", "weebishly", "beautifully", "softly", "quickly", "awkwardly", "inhumanely", "distractedly", "thoughtfully", "slowly", "digitally", "stupidly", "loudly"]

Verbs = ["danced", "simped", "sang", "texted", "fell", "jumped", "twirled", "broke", "sobbed", "laughed", "lied", "nodded", "wriggeled", "hula hooped"]

Verbs_alt = ["threw", "danced with", "played Among Us with", "picked up", "chatted with", "punched", "sang with", "texted", "jumped over"]
# ^ used as a list for verbs that need two people

Nouns = ["human", "weeb", "prune", "cupcake", "rose", "ball", "toy", "brain", "phone", "boy", "girl", "block", "computer", "mug", "cup", "cord", "frog", "cat", "dog", "furby", "tamagachi", "pokemon", "bow", "inchworm", "riddle", "cereal", "banana", "chocolate"]


'''
These all work about the same way

Pseudocode version:

define the function 'get <wordtype> (no parameters)'
{
    return the <random number>th word from the list <wordtype>
}
'''
def getnoun():
    return(Nouns[randint(0, len(Nouns) - 1)])

def getname():
    return(Names[randint(0, len(Names) - 1)])

def getadjective():
    return(Adjectives[randint(0, len(Adjectives) - 1)])

def getadverb():
    return(Adverbs[randint(0, len(Adverbs) - 1)])

def getverb(verbtype):
    if verbtype == 1:
        return(Verbs[randint(0, len(Verbs) - 1)])
    elif verbtype == 2:
        return(Verbs_alt[randint(0, len(Verbs_alt) - 1)])
    else:
        return("error")

def getnoun():
    return(Nouns[randint(0, len(Nouns) - 1)])

#This thing makes the sentences
def createsentence():
    sentencetype = randint(0, len(Verbs_alt))
    #rolls a dice to chose what type of sentence to do

    #was that number the lowest number?
    if sentencetype == 0:
        #if it was, do this code
        #returns a sentence akin to "The adjective noun named name verbed together with the adjective noun named name adverbly."
        return("The " + getadjective() + " " + getnoun() + " named " + getname() + " " + getverb(2) + " the " + getadjective() + " " + getnoun() + " named " + getname() + " " + getadverb() + ".")
    else:
        #if it wasn't, do this code
        #returns a sentence akin to "The adjective noun named name verbed adverbly."
        return("The " + getadjective() + " " + getnoun() + " named " + getname() + " " + getverb(1) + " " + getadverb() + ".")

#Was a secret devcode entered?
if type == "1":
    #this code runs if one was
    while 1==1:
        print(createsentence())
        print("")
        sleep(2)
else:
    #this code runs if no devcode was entered
    while 1 == 1:
        print(createsentence())
        print("Press enter to get another sentence ", end="\r")
        input("")
        print("")
