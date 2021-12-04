#List of vowels
vow = ["a", "e", "i", "o", "u", "y"]
#which vowel should I use?
vowtrack = 0

#list of consonants
cons = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Which consonant should I use at the start of the word? (part 2 only)
constrack = 0



#Which consonant should I use in the middle of the word? (parts 1 AND 2)
midconstrack = 0

print(" " +str(vow[vowtrack]) + str(cons[midconstrack]) + "   " + str(vow[vowtrack]) + str(cons[midconstrack]) + "e")

#part 2  cons + vow + cons + e
while 1 == 1:
    
    if constrack >= 26:
        if midconstrack >= 25:
            vowtrack = vowtrack + 1
            midconstrack = 0
        else:
            midconstrack = midconstrack + 1
        constrack = 0
        print(" " + str(vow[vowtrack]) + str(cons[midconstrack]) + "   " + str(vow[vowtrack]) + str(cons[midconstrack]) + "e")

    print(str(cons[constrack]) + str(vow[vowtrack]) + str(cons[midconstrack]) + "   " + str(cons[constrack]) + str(vow[vowtrack]) + str(cons[midconstrack]) + "e")
    constrack = constrack + 1

    


