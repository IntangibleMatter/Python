from random import randint

thing = int(input("1 for hanoi, 2 for sentences "))

def hanoi(n, s, d, a):
    if n==1:
        print("Move disk 1 from source " + s+ " to destination " +d)
        return
    hanoi(n-1, s, d, a)
    print("Move disk " + str(n) + " from source " + s + " to destination " + d)
    hanoi(n-1, s, d, a)

def sentences(n):
    

if thing == 1:
    hanoi(int(input("How many disks would you like? ")), 'A', 'B', 'C')
elif thing == 2:
    sentences()
else:
    sentences()
