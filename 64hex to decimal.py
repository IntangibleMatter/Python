# convert 64 bit signed number to decimal
# Even though OOP is cool I just kinda naturally fall into a procedural paradigm
hextobi = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111"} #Yes i Memorized this, no I will not tell you how because I don't know

def convertnum(num):
    binarystring = ""
    for i in num:
        binarystring.append(hextobi.i) 

convertnum(input("Please input an 8-character string in hexidecimal").lower)
input("press Enter to close")
