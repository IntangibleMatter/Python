#Random question generator

import random

types = ["activity", "preference", "wyr", "morning"]

qtype = random.randint(0, len(types))


verbs1 = ["do", "check", "play", "think", "read", "ponder", "write", "research", "panic about", "cry about", "laugh about", "sing","eat"]

verbs2 = ["hang out", "masturbate", "dance", "laugh", "cry", "panic"]


nouns = ["book", "food", "colour", "drink", "word", "game", "program", "virus"]


wyr1 = ["eat a pack of frozen waffles (still frozen)", "read minds", "defend your family from a mutated bear"]

wyr2 = ["do a month's worth of schoolwork in a day", "be the lone survivor in a zombie apocolypse", "come to terms with the vastness of the universe"]

def nounget():
    nountype = random.randint(0, len(nouns))

    return(nouns[nountype - 1])

def verb1get():
    
    verb1type = random.randint(0, len(verbs1))

    return(verbs1[verb1type - 1])

def verb2get():
    verb2type = random.randintt(0, len(verbs2))

    return(verbs2[verb2type - 1])


def upinmorn():
    return("What's the first thing you " + verb1get() + " when you get up in the morning?")

i = 0

while i <= 5:
    print(upinmorn())
    i = i + 1
