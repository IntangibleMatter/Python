from random import randint

def trigen():
    i = randint(1, 12)
    j = randint(1, 12)

    l = randint(2, 12)

    il = i * l
    jl = j * l

    tri = [[i, j], [il, jl]]

    return(tri)

def equation(trigen):
    tri = trigen[0]
    tril = trigen[1]

    x = randint(0, 3)

    ans = 0

    if x <= 1:
        ans = tri[x]
    else:
        ans = tril[x - 2]

    question(tri, tril, x, ans)

def question(tri, tril, x, ans):
    if x == 0:
        print("Shape A has 2 sides with lengths of x and " + str(tri[1]) + " respectively. A similar shape has sides of " + str(tril[0]) + " and " + str(tril[1]) + ". Assuming these shapes are in the same orientation, what is the value of x? ")
    elif x == 1:
        print("Shape A has 2 sides with lengths of " + str(tri[0]) + " and x  respectively. A similar shape has sides of " + str(tril[0]) + " and " + str(tril[1]) + ". Assuming these shapes are in the same orientation, what is the value of x? ")
    elif x == 2:
        print("Shape A has 2 sides with lengths of " + str(tri[0]) + " and " + str(tri[1]) + " respectively. A similar shape has sides of x and " + str(tril[1]) + ". Assuming these shapes are in the same orientation, what is the value of x? ")
    else:
        print("Shape A has 2 sides with lengths of " + str(tri[0]) + " and " + str(tri[1]) + " respectively. A similar shape has sides of " + str(tril[0]) + " and x. Assuming these shapes are in the same orientation, what is the value of x? ")

    givenans = 0

    while givenans != ans:
        givenans = int(input("x = "))

        if givenans != ans:
            print("incorrect, please try again")

while True:
    equation(trigen())
