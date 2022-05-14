from random import randint

for i in range(70):
    string = ""
    for i in range(70):
        r = randint(0,4)
        if r >= 2:
            string += " "
        else:
            string += str(r)
    print(string)