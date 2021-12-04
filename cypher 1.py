out = " abcdefghijklmnopqrstuvwxyz"
inp = " defghijklmnopqrstuvwxyzabc"

def cypher():
    encrypt = input("what would you like to decrypt? ")
    decrypt = ""
    for i in encrypt:
        decrypt += out[inp.index(i)]
    print(decrypt)
while True:
    cypher()