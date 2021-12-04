from random import randint

i = 0

ips = []

while i < 20:
    text = ""
    j = 0
    k = 0
    while k < 2:
        j = randint(100, 256)
        text += str(j) + "."
        k += 1
    j = randint(100, 256)
    text += str(j)
    print(text)
    print("")
    i += 1


