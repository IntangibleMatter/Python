import random

import time

print("Random word generator")

syl = ["gla", "thu", "fa", "tre", "ju", "fu", "re", "leb", "che", "cha", "gra"]

pre = ["in", "un", "pre", "pro", "de", "ex"]

suf = ["able", "ly"]

con = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "P", "q", "r", "s", "t", "v", "w", "x", "z"]

string = ""

dosuf = random.randint(0, 3)
dopre = random.randint(0, 2)
sylnum = random.randint(1, 7)

randsyl = 0
randpre = 0
randsuf = 0
randcon = 0

def genstartrands():
    dosuf = random.randint(0, 3)
    print("Dosuf = " + str(dosuf))
    dopre = random.randint(0, 2)
    print("dopre = " + str(dopre))
    sylnum = random.randint(1, 7)
    print("sylnum = " + str(sylnum))

def gennewrands():
    randsyl = random.randint(0, len(syl) - 1)
    print("randsyl = " + str(randsyl))
    randpre = random.randint(0, len(pre) - 1)
    randsuf = random.randint(0, len(suf) - 1)
    randcon = random.randint(0, len(con) - 1)

    
i = 0
def randword():
    i = 0
    string = ""
    genstartrands()
    gennewrands()

    if dopre == 1:
        string = string + str(pre[randpre])

    while i <= sylnum:
        string = string + str(syl[randsyl])
        i = i + 1
        gennewrands()

    if dosuf == 1:
        string = string + con[randcon]
        string = string + suf[randsuf]
    elif dosuf == 2:
        string = string + con[randcon]
    print("New word: " + string)
    
    time.sleep(2)

while True:
    randword()


         
